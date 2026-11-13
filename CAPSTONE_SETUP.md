# Unit 9 capstone: TakeMeter operational extension

**Extension scope:** Shape A (deploy and instrument), Path B (local with logs). This extends the **existing TakeMeter baseline/evaluation command** by wrapping it in a reproducible run path that writes structured logs, measures elapsed wall time, and records failures. It does not retrain the classifier or add labels. Model quality is unchanged.

**Important:** This is an additive file pack for your existing GitHub repository, **not a replacement repository**. Copy `capstone_runner.py`, `capstone_report.py`, and the `tests/` folder into its root. The original `baseline.py`, `results.json`, `test_split.csv`, and `requirements.txt` remain unchanged.

## Running it

From a clean checkout of **your original repository**:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python test.py
python capstone_runner.py -- python baseline.py --trained results.json
python capstone_report.py capstone_runs.jsonl
```

The single command that launches the extended system is `python capstone_runner.py -- python baseline.py --trained results.json` after setup. Python 3.11-3.13 are supported by the original requirements. The repo's original pinned *ranges* are still authoritative; this pack adds no third-party dependencies. The original `RUNNING.md` describes memory/disk/model downloads and requirements. The baseline model downloads on first use (~1.6 GB per the original documentation). This environment cannot verify a clean checkout, model file size, or runtime on your hardware.

Try a deliberately bad command to test failure logging:

```bash
python capstone_runner.py --label deliberate-error -- python -c 'import sys; sys.exit(2)'
```

Try a timeout:

```bash
python capstone_runner.py --timeout 0.01 --label deliberate-timeout -- python -c 'import time; time.sleep(1)'
```

Each command appends one JSON line to `capstone_runs.jsonl`, including timestamp, input command, output/exit status, duration, and any error. **Do not commit `capstone_runs.jsonl` until you have reviewed it for sensitive inputs or output.** The course requires at least ten *real model-system* log entries pasted as text into the README; unit-test logs and deliberately simulated commands do not substitute for those entries.

## What to add to your existing README.md (at its end)

```markdown
## Capstone

**What This Extends**
TakeMeter's existing local model evaluation. I added an operational wrapper that records real runs, timing, and failures without changing model decisions.

**The Shape**
Shape A — deploy and instrument. Out of scope: model retraining, new label categories, hosting a web app.

**Running It**
Path B — local with logs. See `RUNNING.md` and `CAPSTONE_SETUP.md` for commands, environment, and model requirements.

**Instrumentation**
Every JSONL record has timestamp, input, output, duration_seconds, and error.
PASTE AT LEAST TEN REAL ENTRIES FROM `capstone_runs.jsonl` HERE, plus a failure entry or a clear explanation if none occurred.

**What It Costs**
AFTER TEN REAL MODEL RUNS: mean wall-clock time = ___ seconds per run.
Method: `python capstone_report.py capstone_runs.jsonl`. For 100 sequential runs: ___ × 100 = ___ seconds (not API dollars).

**Run Log and Verdicts**
PASTE five-criterion BEFORE table (three trials per criterion), exact outputs, MET/MISSED, and diagnoses here.

**The Improvement**
AFTER diagnosing the before results: describe one narrowly targeted change. Paste the AFTER table (three trials per criterion) and compare it with before.

**What's Still Broken**
Explain each remaining miss, why you stopped, and the first next fix.

**How I Used AI**
Document two specific AI interactions, what came back, and what you changed or rejected. One example is requesting code scaffolding for the capstone runner; record your actual review and modifications honestly.
```

Your original `criteria.md` is from Unit 5. **Do not overwrite or delete it.** Add a clear `## Unit 9 Capstone` section with your five *own* numbered criteria and reasoning, or move the old requirements under a clearly titled legacy section and put the current five at the top. Commit this criteria change **before** collecting acceptance-test results. The course explicitly says to author those criteria yourself, so no proposed criteria are filled in for you here.

## Test and commit sequence

1. Decide on your five criteria (at least three measure logging/deployment extension, one tests a bad path). Write targets and system-specific reasons. Commit `criteria.md` before your acceptance run results.
2. Copy these files; run `python -m unittest discover -s tests -v`. These are engineering tests of the wrapper, **not** acceptance results.
3. Commit operational code in at least three build-phase commits (e.g. runner, report, unit tests). Use the same existing repository.
4. Run the actual extended command repeatedly; capture at least ten real logs, including a failure-path test. Record an average of ten relevant runs, with the measurement method.
5. For your own five criteria, perform three independent trials each, record output, and give a verdict and diagnosis.
6. Make one change based on an observed failure, then perform the same trials again. Do not replace the before data. Log and discuss regressions.
7. Fill in every `## Capstone` README section. The course expects at least eight new commits from this unit and the criteria commit to precede the results commit.

**Evidence status:** Unit tests in this pack can be run in a small environment, but the actual TakeMeter baseline model has **not** been downloaded or executed here. Do not treat unit-test results as proof of real classifier performance.
