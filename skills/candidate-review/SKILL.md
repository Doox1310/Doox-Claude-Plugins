---
name: candidate-review
description: Score a job candidate from the CV and the interview transcript the user hands over — against the saved evaluation framework, with the evidence and its source behind every line, and a shortlist when several candidates arrive at once. Use when the user sends a CV, a hồ sơ ứng viên or an interview recap and asks to đọc, đánh giá, chấm, so sánh or đề cử nhân sự. Reads only what the user supplied.
---

# Candidate Review

## 1. When to use

The user hands over a candidate's material — a CV, a transcript or recording of an interview, a recap
someone typed up — and asks for an assessment.

Not for contractors: a hồ sơ năng lực nhà thầu is `bid-review`, a different framework and a
different question. This skill assesses **a person for a job**.

Read-only, no identity gate, writes no file. The output is tables in the chat reply. A user wanting
it as a file asks, and it is a new file.

## 2. Input

Two kinds of material, either one alone is enough to start:

- **CV** — any format the user sends.
- **Interview** — a transcript in text, a recap someone wrote, or an audio file.

**Audio:** try to read it. If the harness cannot, say so plainly — "không đọc được file âm thanh
này, anh/chị gửi bản transcript dạng text giúp em" — and stop. Never guess at what an interview
contained, and never proceed on the CV alone while pretending the interview was covered.

Only one of the two supplied: assess on it and say which nhóm could not be scored for lack of the
other. A CV alone can never score §3 Xử lý vấn đề; an interview alone rarely evidences §0 and §1.

## 3. The three rules

**3.1 — Bằng chứng, không phải ấn tượng.** Every mức given names the text it came from and where it
came from: `CV, mục Kinh nghiệm` or `phỏng vấn, đoạn nói về dự án X`. A score with no quotable
source behind it does not go in the table.

**3.2 — Tự khai là tự khai.** A CV asserting five years of something is a claim, not a fact. Marked
`Chưa xác minh` unless the material evidences it — a project named, a certificate, a figure the
candidate could not invent, or the interview holding up under detail. Marketing language in a CV
scores nothing on its own, the same way a contractor's brochure scores nothing in `bid-review`.

**3.3 — Thiếu dữ liệu là một kết quả, không phải điểm thấp.** `Chưa đủ dữ liệu` and `Không đạt` are
different findings and must never be merged. One says the candidate failed, the other says the
process did. The gaps go in the "câu hỏi cần làm rõ" section so the next round can close them.

**No inference about the person beyond the material.** Not tính cách from a CV layout, not năng lực
from a school name, not thái độ from một câu trả lời ngắn. Age, giới tính, tình trạng hôn nhân,
quê quán, ảnh chân dung — not scored, not commented on, not carried into the output at all, even when
the CV volunteers them.

## 4. The framework

Read `assets/khung-danh-gia-nhan-su.md` and follow it — the mandatory conditions, the groups, the
four levels, the required output sections. That file is the framework; this skill holds no copy.

It is currently a **bản tạm**. Say so once at the end of the first assessment in a session — "khung
đánh giá đang là bản tạm, anh/chị sửa lại file khung nếu công ty đã có bộ tiêu chí riêng" — so nobody
mistakes the result for a scoring the company signed off on. Once per session, not once per candidate.

**Điều kiện bắt buộc are position-specific.** Ask the user what the vị trí requires before scoring §0
if they have not said. Do not invent a requirement, and do not skip §0 because it was not stated —
a candidate scored well and then rejected on a condition nobody checked is the worst outcome here.

## 5. Several candidates at once

Score each one separately and in full first, then add the comparison. Same framework, same groups,
same order for everyone — a criterion applied to one candidate and not another makes the whole
ranking meaningless.

Rank only those who passed §0. More than 3 candidates: đề cử tối đa 3. More than 5: tối đa 5. Nobody
passed: say nobody passed, and do not promote the least-bad to fill the list.

## 6. Output

Per the framework's "Đầu ra bắt buộc" section, in the chat reply. End with the gaps: which nhóm are
`Chưa đủ dữ liệu`, and what material would close them.

The assessment is input to a human decision, never the decision. Do not write that a candidate should
be hired or rejected — write what the material shows, what it does not, and what is still worth
asking.

**The framework's `Kết luận` is not the exception to that.** `Đề cử` / `Cân nhắc` /
`Không phù hợp` say how far the material carried the candidate against the framework — they are the
sanctioned vocabulary for that reading and nothing more. Write the label, write the evidence behind
it, and stop: no `nên tuyển`, no `nên loại`, no offer, no ranking presented as a decision. `Đề cử`
means the material supports putting them forward; the person who hires still decides.

**`Chưa đủ dữ liệu` at §0 is a third outcome, not a failure.** §5 ranks those who passed §0 and says
what to do when nobody passed; a §0 that could not be scored at all — because the position's điều
kiện bắt buộc were never stated — is neither. Print the per-candidate assessments in full, say plainly
that no ranking can be issued until §0 is settled, and name what would settle it. Never convert an
unscoreable §0 into a pass so the ranking can be produced, and never into a fail.
