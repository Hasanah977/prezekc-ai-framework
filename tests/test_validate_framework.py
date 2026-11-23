"""Regression tests for PREZEKC framework validation."""

import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from validate_framework import CORE_FILES, validate, frontmatter, strip_fences


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for path in CORE_FILES:
            file = self.root / path
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text('# Document\n', encoding='utf-8')

    def create_skill(self, folder='example', name='example', description='A real description.'):
        file = self.root / 'skills' / folder / 'SKILL.md'
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(f'---\nname: {name}\ndescription: >\n  {description}\n---\n# Skill\n', encoding='utf-8')
        return file

    def test_valid_skill(self):
        self.create_skill()
        self.assertEqual([], [f for f in validate(self.root) if f.severity == 'ERROR'])

    def test_missing_frontmatter(self):
        file = self.create_skill()
        file.write_text('# Skill\n', encoding='utf-8')
        self.assertTrue(any('frontmatter' in f.message for f in validate(self.root)))

    def test_name_directory_mismatch(self):
        self.create_skill(folder='example', name='other')
        self.assertTrue(any('directory name' in f.message for f in validate(self.root)))

    def test_broken_local_link(self):
        (self.root / 'README.md').write_text('# Intro\n[Missing](docs/no.md)\n', encoding='utf-8')
        self.assertTrue(any('Broken local link' in f.message for f in validate(self.root)))

    def test_external_link_ignored(self):
        (self.root / 'README.md').write_text('# Intro\n[External](https://example.com/page)\n', encoding='utf-8')
        self.assertFalse(any('Broken local link' in f.message for f in validate(self.root)))

    def test_code_fences_ignored(self):
        (self.root / 'README.md').write_text('# Intro\n```md\n[Fake](missing.md)\n```\n', encoding='utf-8')
        self.assertFalse(any('Broken local link' in f.message for f in validate(self.root)))

    def test_multiline_description(self):
        metadata = frontmatter('---\nname: example\ndescription: >\n  Analyze processes and\n  record evidence.\n---\n# Example\n')
        self.assertIn('record evidence', metadata['description'])

    def test_no_heading_inside_code(self):
        self.assertEqual('', strip_fences('```md\n# Fake heading\n```\n').strip())

    def test_strict_finds_missing_skills(self):
        self.assertTrue(any('Expected skill is missing' in f.message for f in validate(self.root, strict=True)))


if __name__ == '__main__':
    unittest.main()
