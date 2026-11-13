"""Summarize actual structured runs for a TakeMeter capstone submission."""
import argparse
import json
from pathlib import Path
from statistics import mean


def report(path: Path) -> dict:
    records = []
    for line_no, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
            if not isinstance(item.get('duration_seconds'), (int, float)):
                raise ValueError('missing numeric duration_seconds')
            records.append(item)
        except (ValueError, TypeError) as exc:
            raise ValueError(f'invalid log record on line {line_no}: {exc}') from exc
    if not records:
        raise ValueError('log has no records')
    durations = [r['duration_seconds'] for r in records]
    return {
        'runs': len(records),
        'successful': sum(r['output']['status'] == 'ok' for r in records),
        'failed_or_timed_out': sum(r['output']['status'] != 'ok' for r in records),
        'average_wall_seconds_per_run': round(mean(durations), 6),
        'total_wall_seconds': round(sum(durations), 6),
        'projected_wall_seconds_for_100_sequential_runs': round(mean(durations) * 100, 4),
        'note': 'Elapsed wall-clock time, not metered API dollars or CPU seconds.',
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('log', nargs='?', type=Path, default=Path('capstone_runs.jsonl'))
    args = parser.parse_args()
    print(json.dumps(report(args.log), indent=2))


if __name__ == '__main__':
    main()
