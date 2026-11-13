import json
import sys
import tempfile
import unittest
from pathlib import Path

from capstone_runner import run
from capstone_report import report


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.log = Path(self.tmp.name) / 'events.jsonl'

    def tearDown(self):
        self.tmp.cleanup()

    def test_success_creates_structured_record(self):
        result = run([sys.executable, '-c', 'print("analysis")'], log_file=self.log)
        self.assertEqual('ok', result['output']['status'])
        self.assertIn('analysis', result['output']['stdout_tail'])
        self.assertEqual(result, json.loads(self.log.read_text().strip()))

    def test_failure_creates_record(self):
        result = run([sys.executable, '-c', 'raise SystemExit(4)'], log_file=self.log)
        self.assertEqual('error', result['output']['status'])
        self.assertEqual(4, result['output']['exit_code'])
        self.assertEqual(1, report(self.log)['failed_or_timed_out'])

    def test_timeout_creates_record(self):
        result = run([sys.executable, '-c', 'import time; time.sleep(1)'],
                     log_file=self.log, timeout=0.02)
        self.assertEqual('timeout', result['output']['status'])

    def test_empty_input_creates_record(self):
        result = run([], log_file=self.log)
        self.assertEqual('error', result['output']['status'])
        self.assertIn('command', result['error'])

    def test_success_and_failure_append(self):
        run([sys.executable, '-c', 'print(1)'], log_file=self.log)
        run([sys.executable, '-c', 'raise SystemExit(2)'], log_file=self.log)
        self.assertEqual(2, len(self.log.read_text().splitlines()))
        self.assertEqual(2, report(self.log)['runs'])


if __name__ == '__main__':
    unittest.main()
