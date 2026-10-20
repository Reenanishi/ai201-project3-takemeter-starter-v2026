# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## Unit 5 Bonus Features

I plan to attempt all three Unit 5 stretch features:
1. Fourth label (+1 point): I will develop a fourth label if the posts in my chosen community show a distinct category that the first three labels do not capture. I will explain its definition, give two real examples, and document why the other labels were insufficient.
2. Second training run (+1 point): After completing the first training run, I will run the model again with exactly one hyperparameter changed. I will record the original and updated metrics, calculate the numerical differences, and explain what changed.
3. 50 extra examples for the thinnest label (+1 point): I will first collect and label 200 real posts and record the count for each label. Then I will identify the label with the fewest examples and collect at least 50 additional posts for that label. I will document their source, the updated label counts, and how the additional examples affected the dataset and training results.
Declaration status: These are planned stretch features. They have not yet been implemented.


## What This Does



<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->



---

## Label Taxonomy

### `analysis`

**Definition:** Makes an argument about the film backed by a specific, checkable detail — a line of dialogue, a plot event, a date, a production fact — even if the post never lands on a firm conclusion.

**Example 1:**
> "You see, the boss of a crime family would always need a guy with a funeral parlor... Bonasera's beautiful daughter goes out with a couple of punks... The judge suspends the sentence. The judge. A judge in New York in the 1940s giving a suspended sentence for that kind of beating? ... He says, 'Someday, and that day may never come, I'll call upon you to do a service for me.'" — *The Godfather* board, on how Vito manipulated Bonasera

**Example 2:**
> "The Joker's plans require so many coincidences that it beggars belief, such as his phone-bomb escape from the police station... The Two-Face makeup effects on Eckhart also look ridiculous... He's missing the skin on half his face, with his bare eyeball, muscle, bone and tendons exposed... He would have been dead from shock or an infection in minutes." — *The Dark Knight* board, reply in "Massively Overrated Movie"

### `hot_take`

**Definition:** States a confident verdict about the film with no checkable detail offered in support — just the claim.

**Example 1:**
> "1. Bale sucked as Batman... 2. Maggie Gyllenhaal - simply not attractive enough... 3. Dialogue - some of the dialogue is absolute cringe and clunky as hell... 4. The score is completely generic and forgettable" — *The Dark Knight* board, "Massively Overrated Movie" (opening post)

**Example 2:**
> "Nobody exposed the plagiarism and the lack of original ideas, not to mention the absolute lack of artistic quality... cinema is in big trouble..." — *Pulp Fiction* board, "A lot of hype and a lot of mannerism: the most overrated movie of the last 30 years?"

### `reaction`

**Definition:** A short, immediate personal response to the film or to another post, with no argument attached.

**Example 1:**
> "Bingo" — *The Dark Knight* board, reply to "Massively Overrated Movie"

**Example 2:**
> "I disagree." — *The Dark Knight* board, reply to "Massively Overrated Movie"

### `theory`

**Definition:** Poses an open question or possible interpretation without citing anything concrete to support either side — invites the thread to work it out from scratch.

**Example 1:**
> "I mean, the guy is clearly a dumbass. How did he even manage to scrape together $6 million?" — *The Room* board, "How did Tommy even have $6 million to spend on this movie?"

**Example 2:**
> "I wonder if there's a theory that Wallace had Jules clipped for trying to leave." — *Pulp Fiction* board, "Could Jules really have left the life?"

### The hardest boundary

**Which two labels:** `analysis` vs. `theory`

A real post from my reading sits right on this line — *Whiplash* board, "Was Fletcher actually a cruel person?": "Fletcher (to me) implied his drill instructor narcissism was all an act at the coffee shop when he calmly explained... You also see him hug his friend and kindly greet his friend's daughter... Then again, it's also very possible that his calm nature was an act since he tries to sabotage (or test) Andrew's performance in the finale." It cites three specific, checkable scenes (the coffee-shop talk, the hug, the finale sabotage) but never settles on an answer ("I don't know if...").

**The decision rule I used every time:** If a post points to specific, checkable details from the film to build its case, it's `analysis` — even if it never lands on a firm conclusion. `theory` is reserved for posts that pose the open question without citing anything concrete to support either side. Under this rule, the Fletcher post is `analysis`.

I stress-tested both this rule and the taxonomy as a whole with 8 AI-generated posts written to sit on each boundary (e.g. "That twist wrecked me, not in a good way" → `reaction`, a first-person feeling rather than a general verdict about the film; "Wonder if the necklace in the final shot matches the flashback" → `analysis` despite the question-mark phrasing, since it names a checkable detail). All 8 classified cleanly under the definitions above without needing further changes.



---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:**

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->

**Counts per label:**

| Label | Count | Share |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
| **Total** |  | 100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**2.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**3.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Pre-labelling disclosure:**

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
