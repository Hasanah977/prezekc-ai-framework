"""PREZEKC v0.2.0 expansion tests; uses Python standard library only."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V020FeatureTests(unittest.TestCase):
    def test_new_skills_have_matching_frontmatter(self):
        for name in ('ui-ux-flow', 'task-breakdown'):
            content = (ROOT / 'skills' / name / 'SKILL.md').read_text(encoding='utf-8')
            self.assertTrue(content.startswith('---\n'))
            self.assertIn(f'name: {name}', content)
            self.assertIn('version: 0.2.0', content)

    def test_companion_templates_exist(self):
        self.assertTrue((ROOT / 'templates' / 'ui-ux-flow.md').is_file())
        self.assertTrue((ROOT / 'templates' / 'task-breakdown.md').is_file())

    def test_next_step_contract_is_present(self):
        content = (ROOT / 'core' / 'next-action.md').read_text(encoding='utf-8')
        self.assertIn('Recommended next action', content)
        self.assertIn('owner', content.lower())

    def test_bootstrap_single_project_and_refuse_overwrite(self):
        with tempfile.TemporaryDirectory() as t:
            project = Path(t) / 'application'
            project.mkdir()
            cmd = [sys.executable, str(ROOT / 'tools' / 'prezekc.py'), 'init', '--project', str(project)]
            run = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            self.assertTrue((project / 'AGENTS.md').exists())
            self.assertTrue((project / '.prezekc/framework/skills/ui-ux-flow/SKILL.md').exists())
            run2 = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(run2.returncode, 0)

    def test_bootstrap_preserves_existing_project_agent_rules(self):
        with tempfile.TemporaryDirectory() as t:
            project = Path(t) / 'application'
            project.mkdir()
            (project / 'AGENTS.md').write_text('# Existing project policy\n', encoding='utf-8')
            cmd = [sys.executable, str(ROOT / 'tools' / 'prezekc.py'), 'init', '--project', str(project)]
            run = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual((project / 'AGENTS.md').read_text(encoding='utf-8'), '# Existing project policy\n')


if __name__ == '__main__':
    unittest.main()
