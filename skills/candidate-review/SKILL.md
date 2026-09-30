---
name: candidate-review
description: "Score a job candidate from the CV and the interview transcript the user hands over — against the saved evaluation framework, with the evidence and its source behind every line, and a shortlist when several candidates arrive at once. Use when the user sends a CV, a hồ sơ ứng viên or an interview recap and asks to đọc, đánh giá, chấm, so sánh or đề cử nhân sự. Reads only what the user supplied. Load `using-doox` first. Assesses people only — a contractor's hồ sơ năng lực or a quote is `bid-review`."
---

# Candidate Review

**`using-doox` is loaded first and routes here.** This skill uses from it only "Language"; it runs no identity gate and opens no plan file.

## Hard limits

- Read only the material the user supplied; never a plan file; never guess what an interview contained.
- **Evidence and its source behind every score** (§3.1); a mức with no quotable source is not given.
- **No score from absence**: `Chưa đủ dữ liệu` is never `Không đạt`, and never a pass (§3.3).
- Self-declared is self-declared (§3.2).
- **No protected attributes, no inference beyond the material**: age, giới tính, tình trạng hôn nhân,
  quê quán, ảnh chân dung are not scored, not commented on, not carried into the output — even when
  the CV volunteers them. No tính cách from a CV layout, năng lực from a school name, thái độ from one
  short answer.
- No position requirement invented; §0 never skipped or converted to pass/fail when unscoreable.
- Never write that a candidate should be hired or rejected (§6).
- The framework `assets/khung-danh-gia-nhan-su.md` is followed in content.
- Output: chat plus one new local file, never overwriting (§6).

## 1. When to use

The user hands over a candidate's material — CV, interview transcript or recording, a typed recap — and
asks for an assessment of **a person for a job**. A contractor's hồ sơ năng lực is `bid-review`.

## 2. Input

Either is enough to start:

- **CV** — any format, with any giấy tờ attached (bằng lái, trích lục, giấy khám, chứng chỉ, kết quả
  lái thử); drivers often send these instead of a CV.
- **Interview** — transcript, recap, or audio.

**Audio** the harness cannot read: say so ("không đọc được file âm thanh này, anh/chị gửi bản
transcript dạng text giúp em") and stop — never proceed on the CV while implying the interview was
covered.

One of the two only: assess on it and name the nhóm it cannot score — a CV alone never scores B3 Xử lý
vấn đề or A3 Phục vụ khách; an interview alone rarely evidences §0 or licences and certificates.

## 3. The three rules

**3.1 — Bằng chứng, không phải ấn tượng.** Every mức names its text and where: `CV, mục Kinh nghiệm`,
`phỏng vấn, đoạn nói về dự án X`.

**3.2 — Tự khai là tự khai.** "Năm năm kinh nghiệm" in a CV is `Chưa xác minh` unless the material
evidences it — a named project, a certificate, a figure the candidate could not invent, an interview
that holds up under detail. Marketing language scores nothing.

**3.3 — Thiếu dữ liệu là một kết quả, không phải điểm thấp.** `Chưa đủ dữ liệu` says the process
failed, `Không đạt` that the candidate did. Gaps go into "câu hỏi cần làm rõ" so the next round can
close them.

## 4. The framework

Follow `assets/khung-danh-gia-nhan-su.md` — mandatory conditions, groups, four levels, required output.
This skill holds no copy.

It is a **bản nháp**: say so once per session, at the end of the first assessment ("khung đánh giá đang
là bản nháp, anh/chị sửa lại file khung nếu công ty đã có bộ tiêu chí riêng"), so nobody takes it as a
company-approved scoring.

**Nhánh from the vị trí:** tài xế / kỹ thuật viên → A; everything else → B. Unclear (trưởng xưởng,
giám sát đội xe) — ask; never score one candidate on both.

**Điều kiện bắt buộc are position-specific.** Unless stated, ask before scoring §0: which items apply,
thresholds, thị trường (fixes C1's languages), and for a foreign candidate whether C2 giấy phép lao
động is theirs or the company's to obtain — a candidate scored well then rejected on an unchecked
condition is the worst outcome here.

## 5. Several candidates at once

Score each fully first, then compare — same framework, nhánh, groups and order for all, or the ranking
means nothing. Rank only those who passed §0. Default shortlist: >3 candidates → đề cử tối đa 3; >5 →
tối đa 5. Nobody passed: say so; never promote the least-bad.

## 6. Output

Per the framework's "Đầu ra bắt buộc", in the chat, ending with the gaps: which nhóm are `Chưa đủ dữ
liệu` and what material would close them.

Then the same content as a new local file (`using-doox` hard limit 7):
`Đánh giá ứng viên [Họ tên] [Vị trí] dd_mm_yyyy.docx` — `.md` only if `.docx` cannot be produced; an
existing name gets ` (2)`, ` (3)`… The file carries nothing the chat may not.

The assessment is input to a human decision, never the decision: what the material shows, what it does
not, what is worth asking. The framework's `Đề cử` / `Cân nhắc` / `Không phù hợp` only say how far the
material carried the candidate against the framework — write the label and its evidence, and stop: no
`nên tuyển`, `nên loại`, offer, or ranking presented as a decision.

**`Chưa đủ dữ liệu` at §0 is a third outcome.** When the position's điều kiện bắt buộc were never
stated, print every assessment in full, say no ranking can be issued until §0 is settled, and name what
would settle it.
