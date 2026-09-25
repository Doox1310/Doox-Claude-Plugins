---
name: competitor-research
description: Use when a user asks how we compare against competitors in an electric-taxi market — so sánh đối thủ cạnh tranh, mình so với đối thủ, đối thủ taxi/gọi xe, competitor comparison or benchmark, competitive position, Grab/Bolt/Uber/Yango/local taxi firms, analyse de la concurrence — for a named country or city. Produces an RX2 like-for-like comparison `.docx` (own side vs competitors on ten fixed dimensions), or a competitor landscape when our own side is not supplied.
---

# Competitor Research — so sánh mình với đối thủ

**Load `research-method` first** (`../research-method/SKILL.md`, beside this skill's Base
directory). Claims and statuses (§4), source classes (§5), freshness (§8), search, budget and dispatch
(§9), ledger and cache (§10), normalisation and `<RM>/references/metrics.md` (§11), audit (§13) and reply
counts (§14) all come from there. Scope questions (market, data-lock date, mode) follow
`market-research` §2; a request that also evaluates the market or searches contractors is **one** run
with one ledger (`research-method` §1).

`<RM>` below = the absolute path of the `research-method` directory.

## 7. What this skill does

It answers **"where do we stand against them, on what evidence, and where does that leave us
exposed"** — for an electric-taxi operator that runs its own fleet, against the other ways the same
rider gets the same trip. A list of competitors with their fleet sizes is the input, not the output.

**Before starting, read `references/competitor-comparison.md` and follow it.** It carries the
own-side rule (§7.1 — never inferred from model knowledge), the competitor buckets and enumeration
frames C1–C7 (§7.2), the ten comparison dimensions D1–D10 (§7.3), unit normalisation and the
active-vs-announced split (§7.4), the asymmetry rule (§7.5), the four-part output (§7.6), the
boundaries and budget (§7.7), and audit F (§13F). Lenses R05 (competitor landscape) and R06
(competitor strategy) in `<RM>/references/topic-lenses.md` govern the claims; D-rows read their
metric definitions from `<RM>/references/metrics.md`.

Do not attempt the comparison from this summary: the two failures it exists to prevent — comparing a
registered or licensed fleet against an active one, and counting announced vehicles as operating
vehicles — both look like ordinary tables until someone acts on them.

## Output

An **RX2** answer (`<RM>/assets/form-research.md`), written to
`Nghiên cứu So sánh đối thủ [Thị trường] dd_mm_yyyy.docx` per `research-method` §1 and summarised in
the reply — never into the workbook, which has no competitor block. The comparison basis is stated
before the table, one column per side on a like-for-like measure, the trade-off conclusion is
conditional, and cells that cannot be made comparable say `Chưa kết luận được` rather than being
forced into a ranking. RX2's `default_length` — one comparison table plus 100–200 words — applies to
the reading of the table (§7.6 part 2); the four parts of §7.6 are the form's appendix-level detail,
and a user-stated length wins.

A missing own-side figure the user can supply is `[INPUT NEEDED: <field>]` in the draft
(`research-method` §1), and `Chưa có dữ liệu nội bộ` in the table.

Every claim still goes through the ledger (§10) like any other claim.

## 13–14. Audit and reply

Run `research-method` §13 gates A–D plus **audit F** (`references/competitor-comparison.md`), then
reply per `research-method` §14. Also state: competitors compared by bucket, which of C1–C3 were
worked, how many D-rows ended `Chưa kết luận được` for lack of competitor data, and whether the
own-side was supplied in full.
