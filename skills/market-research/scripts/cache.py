#!/usr/bin/env python3
"""Cross-run evidence cache for the market-report skill.

A tariff order, a decree or a registry page does not change between two reports
on the same market, but re-opening it costs the same as the first time — and
opened documents are the dominant cost of a run. This stores the evidence
records already extracted from a source, keyed by canonical URL and version,
and answers the only question the cache can safely answer on its own: may this
entry be reused, or must the source be opened again?

Whether the *figure* is current is a separate question the caller answers with
the freshness rules in SKILL.md §7; every stored date is printed back so it can.

    python cache.py add    <cache.jsonl> <records.json>
    python cache.py lookup <cache.jsonl> --as-of YYYY-MM-DD [--claim-type T] [--q TEXT] [--url U]
    python cache.py selftest
"""

import argparse
import json
import sys
import tempfile
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

# Days a cached extraction may be reused before the source must be re-opened.
# Short wherever the current effective version decides the answer, long for
# figures that are canonical once published.
TTL_DAYS = {
    "fx": 1,
    "tariff": 90,
    "fee": 90,
    "tax": 90,
    "law": 90,
    "permit": 90,
    "licence": 90,
    "pricing": 90,
    "statistics": 180,
    "network": 180,
    "contractor": 180,
    "spec": 365,
    "climate": 1825,
}
DEFAULT_TTL_DAYS = 90

REQUIRED = ("url", "publisher", "claim_type", "value", "accessed")
OPTIONAL = ("evidence_class", "scope", "period", "published", "effective", "note")

TRACKING_KEYS = {"fbclid", "gclid", "ref", "ref_src", "igshid", "mc_cid", "mc_eid"}


def canonical(url):
    """Collapse the spellings of one document to a single cache key."""
    parts = urlsplit(url.strip())
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    query = "&".join(
        q
        for q in parts.query.split("&")
        if q and not _is_tracking(q)
    )
    path = parts.path.rstrip("/") or "/"
    # Scheme is not part of a document's identity; a page served on both http
    # and https is one source, not two.
    return urlunsplit(("https", host, path, query, ""))


def _is_tracking(pair):
    key = pair.split("=", 1)[0].lower()
    return key.startswith("utm_") or key in TRACKING_KEYS


def _key(rec):
    """One entry per document version, so a superseded order is not overwritten."""
    return f"{rec['url']}\t{rec.get('effective') or rec.get('published') or ''}"


def load(cache_path):
    path = Path(cache_path)
    if not path.exists():
        return {}
    entries = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rec = json.loads(line)
            entries[_key(rec)] = rec
    return entries


def add(cache_path, records):
    """Upsert evidence records. Validates the whole batch before touching the file."""
    if isinstance(records, dict):
        records = [records]
    errors = []
    for i, rec in enumerate(records):
        missing = [f for f in REQUIRED if not rec.get(f)]
        if missing:
            errors.append(f"record {i}: missing {', '.join(missing)}")
        for field in ("accessed", "published", "effective"):
            if rec.get(field) and not _parse_date(rec[field]):
                errors.append(f"record {i}: {field}={rec[field]!r} is not YYYY-MM-DD")
    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        raise SystemExit(1)

    entries = load(cache_path)
    added = updated = 0
    for rec in records:
        rec = {k: v for k, v in rec.items() if k in REQUIRED + OPTIONAL}
        rec["url"] = canonical(rec["url"])
        if _key(rec) in entries:
            updated += 1
        else:
            added += 1
        entries[_key(rec)] = rec

    path = Path(cache_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        json.dumps(entries[k], ensure_ascii=False, sort_keys=True)
        for k in sorted(entries)
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    unknown = {r.get("claim_type") for r in records} - set(TTL_DAYS)
    if unknown:
        print(
            f"note: claim_type {sorted(unknown)} not in the TTL table, "
            f"reused for {DEFAULT_TTL_DAYS} days",
            file=sys.stderr,
        )
    print(f"cached {added} new, {updated} updated, {len(entries)} total in {cache_path}")


def _parse_date(text):
    try:
        return date.fromisoformat(str(text))
    except ValueError:
        return None


def lookup(cache_path, as_of, claim_type=None, q=None, url=None):
    entries = load(cache_path)
    as_of_date = _parse_date(as_of)
    if not as_of_date:
        print(f"ERROR: --as-of {as_of!r} is not YYYY-MM-DD", file=sys.stderr)
        raise SystemExit(1)

    wanted_url = canonical(url) if url else None
    needle = q.lower() if q else None
    hits = []
    for rec in entries.values():
        if claim_type and rec.get("claim_type") != claim_type:
            continue
        if wanted_url and rec["url"] != wanted_url:
            continue
        if needle and needle not in " ".join(
            str(rec.get(f, "")) for f in REQUIRED + OPTIONAL
        ).lower():
            continue
        hits.append(rec)

    fresh = 0
    for rec in sorted(hits, key=lambda r: r.get("accessed", ""), reverse=True):
        ttl = TTL_DAYS.get(rec.get("claim_type"), DEFAULT_TTL_DAYS)
        accessed = _parse_date(rec.get("accessed"))
        age = (as_of_date - accessed).days if accessed else None
        if age is not None and 0 <= age <= ttl:
            verdict, fresh = "FRESH", fresh + 1
        else:
            verdict = "STALE"
        age_text = f"age {age}d" if age is not None else "age unknown"
        print(
            f"{verdict}\t{rec.get('claim_type')}\t{age_text} / ttl {ttl}d\t"
            f"class {rec.get('evidence_class', '?')}\t{rec.get('publisher')}"
        )
        print(
            f"\teff {rec.get('effective') or '-'}  pub {rec.get('published') or '-'}  "
            f"acc {rec.get('accessed')}  scope {rec.get('scope') or '-'}  "
            f"period {rec.get('period') or '-'}"
        )
        print(f"\t{rec.get('value')}")
        print(f"\t{rec['url']}")
    print(f"# hits: {len(hits)} (fresh {fresh} / stale {len(hits) - fresh})")


def selftest():
    with tempfile.TemporaryDirectory() as tmp:
        cache = Path(tmp) / "sub" / "evidence.jsonl"
        recs = Path(tmp) / "r.json"

        base = {
            "url": "https://WWW.evn.com.vn/Tariff/2024?utm_source=x&id=7",
            "publisher": "EVN",
            "claim_type": "tariff",
            "evidence_class": "A",
            "value": "2.006,79 VND/kWh giờ bình thường, cấp <6kV, chưa VAT",
            "effective": "2024-10-11",
            "published": "2024-10-11",
            "accessed": "2026-06-01",
        }
        recs.write_text(json.dumps([base]), encoding="utf-8")
        add(cache, json.loads(recs.read_text(encoding="utf-8")))
        stored = load(cache)
        assert len(stored) == 1
        only = next(iter(stored.values()))
        assert only["url"] == "https://evn.com.vn/Tariff/2024?id=7", only["url"]

        # Same document, different spelling and a later access: one entry, not two.
        again = dict(base, url="http://evn.com.vn/Tariff/2024/?id=7&fbclid=z",
                     accessed="2026-08-01")
        add(cache, again)
        assert len(load(cache)) == 1, "canonical URL must collapse to one entry"

        # A new effective version is a new entry, not an overwrite.
        add(cache, dict(base, effective="2025-05-01", accessed="2026-08-01"))
        assert len(load(cache)) == 2, "a superseded version must be kept"

        try:
            add(cache, {"url": "https://x.test/a", "publisher": "X"})
        except SystemExit:
            pass
        else:
            raise AssertionError("a record missing required fields must fail")
        assert len(load(cache)) == 2, "a rejected batch must write nothing at all"

        try:
            add(cache, dict(base, accessed="01/06/2026"))
        except SystemExit:
            pass
        else:
            raise AssertionError("a non-ISO date must fail")

        # tariff ttl is 90 days: 2026-08-01 + 90 = 2026-10-30.
        add(cache, dict(base, claim_type="climate", url="https://imh.test/rain",
                        publisher="IMH", accessed="2024-01-01",
                        value="Lượng mưa trung bình năm 1.800 mm"))
        print("--- lookup 2026-10-30 ---")
        lookup(cache, "2026-10-30")
        print("--- lookup 2026-11-01 ---")
        lookup(cache, "2026-11-01", claim_type="tariff")
        print("--- lookup by text ---")
        lookup(cache, "2026-11-01", q="VND/kWh")
    print("selftest ok")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("add", help="upsert evidence records into the cache")
    p.add_argument("cache")
    p.add_argument("json")

    p = sub.add_parser("lookup", help="find reusable evidence before searching")
    p.add_argument("cache")
    p.add_argument("--as-of", required=True, help="report data-lock date, YYYY-MM-DD")
    p.add_argument("--claim-type")
    p.add_argument("--q", help="substring to match against any stored field")
    p.add_argument("--url")

    sub.add_parser("selftest", help="run the built-in checks")

    args = parser.parse_args()
    if args.cmd == "add":
        add(args.cache, json.loads(Path(args.json).read_text(encoding="utf-8")))
    elif args.cmd == "lookup":
        lookup(args.cache, args.as_of, args.claim_type, args.q, args.url)
    else:
        selftest()


if __name__ == "__main__":
    main()
