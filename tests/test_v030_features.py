"""PREZEKC v0.3.0 contract, quality evidence, and compatibility smoke tests."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V030FeatureTests(unittest.TestCase):
    def test_three_skills_frontmatter(self):
        for name in ('ui-design', 'security-review', 'code-quality'):
            path = ROOT / 'skills' / name / 'SKILL.md'
            content = path.read_text(encoding='utf-8')
            self.assertTrue(content.startswith('---\n'), name)
            self.assertIn(f'name: {name}', content)
            self.assertIn('version: 0.3.0', content)

    def test_new_templates_and_quality_contract(self):
        for path in ('templates/ui-design-review.md', 'templates/security-review.md',
                     'templates/code-quality-review.md', 'core/engineering-quality.md'):
            self.assertTrue((ROOT / path).is_file(), path)

    def test_preserve_v020_baseline(self):
        for path in ('core/next-action.md', 'core/task-execution.md',
                     'skills/prd-generation/SKILL.md', 'skills/prd-to-srs/SKILL.md',
                     'skills/ui-ux-flow/SKILL.md', 'skills/task-breakdown/SKILL.md'):
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertIn('PREZEKC-V030-EXTENSION', (ROOT / 'AGENTS.md').read_text(encoding='utf-8'))

    def test_quality_report_accepted(self):
        mod = self._load_checker()
        data = {'task_id': 'TASK-1', 'baseline': 'SRS-1', 'changed_files': ['test.dart'],
                'checks': [{'name': 'unit', 'status': 'PASS', 'evidence': 'pytest -q: 2 passed'},
                           {'name': 'device', 'status': 'NOT_RUN', 'evidence': 'no emulator'}],
                'open_risks': ['device behavior unchecked'],
                'recommended_next_action': 'run device test'}
        self.assertEqual(mod.check_report(data), [])

    def test_quality_report_rejects_unproven_status(self):
        mod = self._load_checker()
        data = {'task_id': 'X', 'baseline': 'SRS-1', 'changed_files': [],
                'checks': [{'name': 'security', 'status': 'PERFECT', 'evidence': ''}],
                'open_risks': [], 'recommended_next_action': 'review'}
        self.assertTrue(mod.check_report(data))

    @staticmethod
    def _load_checker():
        spec = importlib.util.spec_from_file_location('prezekc_quality_gate', ROOT / 'tools/quality_gate.py')
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        return module


if __name__ == '__main__':
    unittest.main()
