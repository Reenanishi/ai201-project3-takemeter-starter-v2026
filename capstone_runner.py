"""Instrument an existing TakeMeter command without changing the classifier.

Uses only the Python standard library. All attempts, including failures/timeouts,
produce structured JSONL records that can be inspected after execution.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import uuid

DEFAULT_LOG = Path('capstone_runs.jsonl')


def run(command: list[str], *, log_file: Path = DEFAULT_LOG, timeout: float = 600.0,
        input_label: str = 'existing TakeMeter command') -> dict:
    if timeout <= 0:
        raise ValueError('timeout must be greater than zero')
    start_utc = dt.datetime.now(dt.timezone.utc).isoformat()
    started = time.perf_counter()
    status = 'error'
    exit_code = None
    stdout = ''
    stderr = ''
    error = None
    try:
        if not command:
            raise ValueError('command must contain at least one executable')
        result = subprocess.run(command, capture_output=True, text=True,
                                timeout=timeout, check=False)
        stdout, stderr = result.stdout, result.stderr
        exit_code = result.returncode
        status = 'ok' if exit_code == 0 else 'error'
        if exit_code != 0:
            error = f'process exited with code {exit_code}'
    except subprocess.TimeoutExpired as exc:
        status = 'timeout'
        error = f'command exceeded {timeout:g} seconds'
        stdout = (exc.stdout or b'').decode(errors='replace') if isinstance(exc.stdout, bytes) else (exc.stdout or '')
        stderr = (exc.stderr or b'').decode(errors='replace') if isinstance(exc.stderr, bytes) else (exc.stderr or '')
    except (OSError, ValueError) as exc:
        error = f'{type(exc).__name__}: {exc}'
    duration = round(time.perf_counter() - started, 6)
    record = {
        'run_id': uuid.uuid4().hex,
        'timestamp': start_utc,
        'input': {'label': input_label, 'command': command},
        'output': {'status': status, 'exit_code': exit_code,
                   'stdout_tail': stdout[-1000:], 'stderr_tail': stderr[-1000:]},
        'duration_seconds': duration,
        'compute_seconds': duration,  # elapsed wall time; NOT CPU or API billing
        'error': error,
    }
    log_file.parent.mkdir(parents=True, exist_ok=True)
    with log_file.open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + '\n')
    return record


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--log', type=Path, default=DEFAULT_LOG)
    parser.add_argument('--timeout', type=float, default=600)
    parser.add_argument('--label', default='TakeMeter baseline evaluation')
    parser.add_argument('command', nargs=argparse.REMAINDER,
                        help='command after --, e.g. -- python baseline.py --trained results.json')
    args = parser.parse_args(argv)
    command = args.command[1:] if args.command[:1] == ['--'] else args.command
    if not command:
        command = [sys.executable, 'baseline.py', '--trained', 'results.json']
    record = run(command, log_file=args.log, timeout=args.timeout,
                 input_label=args.label)
    print(json.dumps(record, ensure_ascii=False, indent=2))
    return 0 if record['output']['status'] == 'ok' else 1


if __name__ == '__main__':
    sys.exit(main())
