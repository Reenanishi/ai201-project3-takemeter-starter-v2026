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

**Why this target:** I've got four labels, so just guessing randomly gets you about 25% right. 0.55 is well above that, but I'm only training on around 200 posts split 70/15/15, which works out to maybe 35 training examples per label if things stay balanced. That's not a lot for fine-tuning a transformer, so I don't actually expect this to get anywhere near the 80s. I picked 0.55 as the point where I could honestly say the model learned something real, not a number that's just safe to hit.

---

## 2. Per-label performance

Every label's F1 score on the held-out test split is at least **0.40**.

**Why this target:** I'm pretty sure `theory` is going to end up my thinnest label — when I was reading posts for Milestone 1, open questions with nothing backing them up just didn't come up as often as confident one-liners (`hot_take`) or quick agree/disagree replies (`reaction`). With a ~200-row file split 70/15/15, the test set is only something like 30 rows spread across four labels, so my smallest label might only have 6-8 examples sitting in test. At that size, getting even two of them wrong swings the F1 score a lot. 0.40 is really just there to catch "the model didn't learn this label at all" — I'm not expecting every label to barely scrape by at that number.

---

## 3. Balance

In `labels.csv`, no single label's row count exceeds **45%** of the total, and no label's row count falls below **12%** of the total.

**Why this target:** The project only requires staying under 70%, but my four labels really aren't naturally balanced on these boards — `hot_take` and `reaction` posts are everywhere, while `theory`-style open questions and well-argued `analysis` posts are harder to find. Setting a 45% ceiling and a 12% floor (so at least ~24 out of 200 rows) basically forces me to keep going after the thin categories instead of just filling the file with whatever's easiest to grab. If I end up missing this one, that's exactly what my stretch feature — 50 extra examples for the thinnest label — is there to fix.

---

## 4. Consistency

Labeling the 30 posts in `data/staff_posts.csv` under the definitions in `data/staff_taxonomy.md`, my agreement with `data/staff_labels.csv` is at least **60%** (at least 18 of 30 posts match).

**Why this target:** This uses staff's own three-label taxonomy, not mine, and they picked several of the 30 posts specifically because they're genuinely ambiguous between two labels — that's the whole point of having decision rules in the first place. I went with 60% instead of something higher because I'll be applying someone else's rules for the very first time, under a time limit, and I'd rather pick a number I could actually fail than pad it to make sure I pass.

---

## 5. Confidence

Among test-split predictions where the model's top-class confidence is at least 0.70, accuracy on that subset is at least **10 percentage points** higher than overall test accuracy.

**Why this target:** `results.json` records how confident the model was on every single prediction, so this is actually checkable. If the model has any real sense of when it's unsure, its confident guesses should beat its own average by a real margin — not just a point or two, which could easily be noise with how few test examples I'll have per label. 10 points felt like the gap I'd actually trust as real instead of just seed-to-seed luck.

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
