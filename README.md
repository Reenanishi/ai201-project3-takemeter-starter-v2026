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
Declaration status:
1. Fourth label — **done**. `theory` was added in Milestone 2 (see Label Taxonomy below): posts that pose an open question or interpretation with no checkable detail attached showed up distinctly from `analysis`/`hot_take`/`reaction` across the MovieChat boards I read, and the hardest-boundary writeup documents why the other three labels couldn't absorb it.
2. Second training run — not yet implemented (Milestone 5).
3. 50 extra examples for the thinnest label — not yet implemented (depends on label counts from Milestone 4).


## What This Does

I'm building a classifier for posts on moviechat.org — the old IMDb message boards, now running as their own public film discussion forum. I'd originally planned on r/movies, but Reddit kept blocking every tool I tried to use to pull posts from it, so I switched to moviechat.org and collected across 19 different movies' boards instead, to keep things spread out and not centered on any one film.

My classifier sorts each post into one of four labels: `analysis` (backs up its point with something specific and checkable from the movie), `hot_take` (a confident opinion with nothing backing it up), `reaction` (a quick, low-effort emotional reply with no real argument), or `theory` (an open question or interpretation that doesn't point to anything concrete either way).

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

I found a real post from my reading that sits right on this line — *Whiplash* board, "Was Fletcher actually a cruel person?": "Fletcher (to me) implied his drill instructor narcissism was all an act at the coffee shop when he calmly explained... You also see him hug his friend and kindly greet his friend's daughter... Then again, it's also very possible that his calm nature was an act since he tries to sabotage (or test) Andrew's performance in the finale." It points at three specific, checkable scenes (the coffee-shop talk, the hug, the finale sabotage), but it never actually settles on an answer ("I don't know if...").

**The decision rule I used every time:** if a post points to specific, checkable details from the film to make its case, I call it `analysis` — even when it never lands on a firm conclusion. I only use `theory` for posts that pose the open question without pointing at anything concrete on either side. Under that rule, the Fletcher post ends up being `analysis`.

I### Stress Test — 8 Borderline Posts

I used ChatGPT to make 8 example movie posts that were a little confusing to label. I wanted to check if my four labels were clear enough, especially when a post could fit into more than one category.

These are made-up examples for testing, not real MovieChat posts. ChatGPT suggested the labels based on my definitions.

| # | Example post | Label | Reason |
|---|---|---|---|
| 1 | The Joker was definitely the best villain in any Batman movie. Nobody else even comes close. | `hot_take` | It's a strong opinion without specific evidence. |
| 2 | Was Fletcher actually trying to help Andrew? In the final concert, he changes the music without warning, which makes me think he wanted Andrew to fail. | `analysis` | It mentions a specific scene to support an idea. |
| 3 | I agree with you. That ending was disappointing. | `reaction` | It's a short personal response without an explanation. |
| 4 | What if Cobb never woke up at the end of Inception? | `theory` | It asks about a possible interpretation without evidence. |
| 5 | That twist completely shocked me. I couldn't stop thinking about it. | `reaction` | It's a personal feeling about the movie. |
| 6 | The movie is overrated. The acting is bad, and the story is boring. | `hot_take` | It gives opinions but no specific examples. |
| 7 | I think the ending of The Godfather shows Michael becoming like his father. The final scene, where the door closes on Kay, supports that idea. | `analysis` | It uses a specific scene to support an interpretation. |
| 8 | Could Tyler Durden just be a way for the narrator to escape his boring life? | `theory` | It suggests an idea without mentioning evidence. |

The hardest one was Post 2 because it starts with a question, so it could look like `theory`. But it mentions something specific that happened in the movie, so `analysis` fits better.

This test helped me understand that I should look for specific evidence instead of deciding based only on whether a post is written as a question. I didn't change my label definitions after looking at these examples.


---

## The Dataset

**Where the posts came from:** moviechat.org, which is basically the old IMDb message boards running on their own now as a public film forum. I couldn't actually pull from r/movies like I originally planned — Reddit kept getting blocked by my tools no matter how I tried to access it, so I switched communities. I picked moviechat.org because it's the same kind of film-discussion space, fully public, no login needed to read anything. To avoid the "built around one show or release" problem, I didn't just sit on one movie's board — I pulled posts from 19 different films across a bunch of genres and decades (The Dark Knight, Pulp Fiction, Whiplash, The Godfather, The Room, Inception, Fight Club, Parasite, Joker, No Country for Old Men, The Matrix, Titanic, Seven, Memento, Donnie Darko, The Shining, Interstellar, Shutter Island, American Psycho, Get Out, and The Sixth Sense), grabbing the opening post plus the reply chain from one or two threads on each board.

**How I labeled them:** I used Claude to help collect the raw posts and do a first-pass label on most of the rows (188 of 208) against the definitions in `label_definitions.txt`, then I went through and corrected the ones I disagreed with. The last 20 rows (marked `cold` in the note column) I labeled completely by myself, no AI involved — Claude had pulled those posts but never labeled or discussed them with me, so they're my honesty check, exactly like the assignment wants.

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| `reaction` | 61 | 29.3% |
| `analysis` | 57 | 27.4% |
| `hot_take` | 54 | 26.0% |
| `theory` | 36 | 17.3% |
| **Total** | 208 | 100% |

No label goes over the project's 70% cap, or even the tighter 45% ceiling I set for myself in `criteria.md`. `theory` is at 17.3% — above the 12% floor I set, but it's still clearly my thinnest label, which is exactly what I expected after Milestone 1's reading. That's what stretch feature #3 (50 extra examples for the thinnest label) is going to target later.

**Three hard cases**

**1.**
> *The post:* A reply in *The Room*'s "$6 million" thread: "Could also be lottery winners. They tend to waste their money quickly or get killed by the mob (seriously, winning a lottery increases chances of you dying 800% and chances of people around you dying 270%)."
>
> *Could have been:* `analysis`, since it throws out a specific stat, or `hot_take`, since when someone else pushed back and asked "do you have the specific data/quote?" the only source that ever showed up was a random Reddit comment — not anything actually checkable.
>
> *I chose, because:* I went with `analysis`. My rule just says a post needs to name something specific and checkable to build its case — it never said the fact has to actually hold up once someone checks it. That bugged me a little once I sat with it, because a made-up-sounding stat and a real one are getting treated the same way right now. That's a real hole in my taxonomy, not something I papered over.

**2.**
> *The post:* A reply in *Pulp Fiction*'s "Could Jules really have left the life?" thread: "Some people have fan theories that the piano player in Kill Bill (at the wedding, Vol.2) is Jules, walking the earth. I liked that theory for a while, but more and more I think... nah."
>
> *Could have been:* `theory`, because it's basically just weighing a possibility out loud and ends up rejecting it — or `analysis`, because it does point to something specific and checkable (the Kill Bill cameo) to reason through.
>
> *I chose, because:* `analysis`, for the same reason as case 1 — a specific detail wins even when the poster ends up leaning away from their own idea. This is the flip side of case 1: a post can sound like `theory` because of its tone, but still have enough concrete detail in it to count as `analysis`.

**3.**
> *The post:* The opening post of *Fight Club*'s "Why does Tyler put on his seat belt?" thread: "My guess is that Tyler has limits (eg when Narrator shot at the van full of Nitroglycerin, he freaked out) and doesn't want to die... Any thoughts?"
>
> *Could have been:* `theory`, since it's literally phrased as an open question ending in "Any thoughts?" — or `analysis`, since the guess is actually built on a specific scene.
>
> *I chose, because:* `analysis` again — my own decision rule says the checkable detail decides it, not whether the post ends in a question mark. Seeing this pattern show up a third time made me trust that it's a real, consistent gap in how I split `analysis` from `theory`, not just a one-off weird post.

---

## The Training Run

**Base model:** `distilbert-base-uncased`


**Settings:** 3 epochs, learning rate 2e-5, batch size 16, max length 128 tokens, seed 42. Trained on an Apple Silicon GPU (MPS backend), torch 2.14.1.

**Anything I changed from the defaults, and why:** The initial training run used the notebook's default settings. I later completed a second experiment changing only the number of epochs from 3 to 4. I compared both settings using the corrected dataset and the same random seed (42).

**Split sizes:** 144 train / 32 val / 32 test, out of 208 total rows. Per-label counts in the test split:

| Label | Train | Val | Test |
|---|---|---|---|
| `analysis` | 39 | 9 | 9 |
| `hot_take` | 38 | 8 | 8 |
| `reaction` | 43 | 9 | 9 |
| `theory` | 24 | 6 | 6 |

`theory` only has 6 examples in the test split, under the ~8 I flagged as a risk in `criteria.md` — so if its F1 jumps around a lot between seeds next unit, that's not a surprise, it's exactly what I called out ahead of time.


### Bonus Experiment: 3 vs. 4 Epochs

I tested whether increasing training from 3 epochs to 4 would improve my text classification model.

I used the same corrected dataset, model, random seed (42), learning rate (2e-5), batch size (16), and maximum sequence length (128). The only hyperparameter I changed was the number of epochs.

| Metric | 3 Epochs | 4 Epochs |
|---|---:|---:|
| Test examples | 31 | 31 |
| Accuracy | 61.29% | 54.84% |
| Macro F1 | 0.4944 | 0.4489 |

The 3-epoch model performed better. Its accuracy was 6.45 percentage points higher, and its macro F1 was approximately 0.0455 higher.

This experiment taught me that training for more epochs does not always improve performance. Because the test set was small, these results are preliminary.

**Base model:** `distilbert-base-uncased`


**Settings:** 3 epochs, learning rate 2e-5, batch size 16, max length 128 tokens, seed 42. Trained on an Apple Silicon GPU (MPS backend), torch 2.14.1.

**Anything I changed from the defaults, and why:** The initial training run used the notebook's default settings. I later completed a second experiment changing only the number of epochs from 3 to 4. I compared both settings using the corrected dataset and the same random seed (42).




---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:* I used Claude to help gather public MovieChat posts and suggest labels based on my definitions.
- *What came back:*It provided posts and suggested categories such as analysis, hot_take, reaction, and theory.
- *What I changed:* I reviewed the examples using my decision rule and kept my four labels because the rule helped distinguish analysis from theory.

**Moment 2**

- *What I asked for:* I asked ChatGPT to guide me through running my TakeMeter training notebook in VS Code.
- *What came back:* It explained how to select the correct Python environment, run the notebook sections, and check the training output.
- *What I changed:*  ran the notebook on my own computer using my 208-post dataset and recorded the training settings and results in my README.

**Pre-labelling disclosure:** 
I labeled 20 MovieChat posts using my label definitions a cold labeling check. I have read each post, selected the appropriate category, and recorded my decision in labels.csv with cold in the note column.

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
