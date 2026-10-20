# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall accuracy

Overall accuracy on the held-out test split is at least **0.55**, holding across all three seeds in Unit 6.

**Why this target:** My taxonomy has four labels, so a random guesser clears about 25%. 0.55 sits well above that, but I'm training on roughly 200 posts split 70/15/15 — about 140 training rows across four classes, call it 35 per class if I keep things balanced. That's a small amount of data for a transformer fine-tune, so I'm not expecting it to climb into the 80s. 0.55 is the point where I'd honestly call the model better than flipping a four-sided coin, not a number chosen to look good.

---

## 2. Per-label performance

Every label's F1 score on the held-out test split is at least **0.40**.

**Why this target:** `theory` is the label I expect to be thinnest — across the five MovieChat boards I read for Milestone 1, open questions with no supporting detail showed up far less often than confident one-line verdicts (`hot_take`) or bare agreement/disagreement (`reaction`). At 15% of a ~200-row file, the test split is only around 30 rows spread across four labels, so my smallest label could land with as few as 6-8 test examples — at that size, one or two misclassifications swing F1 by a lot. 0.40 is a floor meant to catch "the model never learned this label at all," not a bar I expect every label to just barely clear.

---

## 3. Balance

In `labels.csv`, no single label's row count exceeds **45%** of the total, and no label's row count falls below **12%** of the total.

**Why this target:** The project-wide cap is 70%, but my four labels aren't naturally balanced in the community I'm drawing from — `hot_take` and `reaction` posts are common on these boards, while `theory`-style open questions and well-argued `analysis` posts are rarer. A 45% ceiling and a 12% floor (at least ~24 of 200 rows) force me to keep actively collecting the thin categories instead of letting the easy ones fill the file, which is exactly what my planned stretch feature — 50 extra examples for the thinnest label — exists to fix if I miss it.

---

## 4. Consistency

Labeling the 30 posts in `data/staff_posts.csv` under the definitions in `data/staff_taxonomy.md`, my agreement with `data/staff_labels.csv` is at least **60%** (at least 18 of 30 posts match).

**Why this target:** This set uses staff's own three-label taxonomy, not my four-label one, and staff picked several of the 30 specifically because they're genuinely ambiguous between two labels — the kind of case their own decision rules exist to resolve. I'm setting 60% rather than aiming higher because I'll be applying someone else's written rules for the first time, under time pressure, and I'd rather set a number I can genuinely miss or clear than one padded to be safe.

---

## 5. Confidence

Among test-split predictions where the model's top-class confidence is at least 0.70, accuracy on that subset is at least **10 percentage points** higher than overall test accuracy.

**Why this target:** `results.json` records the softmax confidence behind every prediction specifically so this can be checked. If the model has learned anything about which of its own guesses are shaky, its confident predictions should clearly outperform its average — not just by a point or two, which could be noise given how few test examples land in each label. A 10-point gap is large enough that I'd trust it's real rather than seed-to-seed jitter.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
