"""Contract tests for controlled Markdown requirement extraction."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "extract_requirements.py"
spec = importlib.util.spec_from_file_location("extract_requirements", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
EXAMPLES = Path(__file__).resolve().parents[1] / "examples" / "markdown"


class ExtractRequirementsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prd = (EXAMPLES / "prd.md").read_text(encoding="utf-8")
        cls.srs = (EXAMPLES / "srs.md").read_text(encoding="utf-8")
        cls.rtm = (EXAMPLES / "rtm.md").read_text(encoding="utf-8")

    def test_extract_valid_baselines(self):
        prd = module.extract_prd(self.prd)
        srs = module.extract_srs(self.srs)
        rtm = module.extract_rtm(self.rtm)
        self.assertEqual(prd["approval"]["decision_reference"], "EXAMPLE-DEC-001")
        self.assertEqual(prd["requirements"][0]["priority"], "MUST")
        self.assertEqual(srs["requirements"][0]["parent_requirements"], ["PRD-FR-001"])
        self.assertEqual(rtm["mappings"][0]["design_ids"], [])

    def test_missing_approval_reference_rejected(self):
        with self.assertRaisesRegex(module.ExtractionError, "Decision Reference"):
            module.extract_prd(self.prd.replace("EXAMPLE-DEC-001", "PENDING"))

    def test_mismatched_approved_version_rejected(self):
        with self.assertRaisesRegex(module.ExtractionError, "Approved Version"):
            module.extract_prd(self.prd.replace("| Approved Version | 1.0 |", "| Approved Version | 2.0 |"))

    def test_duplicate_prd_requirement_rejected(self):
        section = "\n#### PRD-FR-001 — Duplicate\n\n**Statement:** Other action.\n\n**Priority:** MUST\n"
        with self.assertRaisesRegex(module.ExtractionError, "duplicate"):
            module.extract_prd(self.prd + section)

    def test_missing_parent_rejected(self):
        with self.assertRaisesRegex(module.ExtractionError, "Parent Requirements"):
            module.extract_srs(self.srs.replace("PRD-FR-001", "PENDING"))

    def test_fenced_examples_ignored(self):
        example = '\n```markdown\n#### PRD-FR-002 — Fabricated\n**Statement:** Fabricated\n**Priority:** MUST\n```\n'
        self.assertEqual(len(module.extract_prd(self.prd + example)["requirements"]), 1)

    def test_duplicate_rtm_mapping_rejected(self):
        row = "| PRD-FR-001 | SRS-FR-001.1 | PENDING | PENDING | PENDING | SRS_MAPPED |\n"
        with self.assertRaisesRegex(module.ExtractionError, "duplicate"):
            module.extract_rtm(self.rtm + row)

    def test_rtm_invalid_design_id_rejected(self):
        with self.assertRaisesRegex(module.ExtractionError, "invalid design"):
            module.extract_rtm(self.rtm.replace("| PENDING | PENDING | PENDING |", "| TC-001 | PENDING | PENDING |"))

    def test_no_source_overwrite_or_overwrite_existing_output(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name, content in [("prd", self.prd), ("srs", self.srs), ("rtm", self.rtm)]:
                (root / f"{name}.md").write_text(content, encoding="utf-8")
            args = ["--prd", str(root / "prd.md"), "--srs", str(root / "srs.md"),
                    "--rtm", str(root / "rtm.md"), "--output", str(root / "out")]
            self.assertEqual(module.main(args), 0)
            self.assertEqual(module.main(args), 1)
            self.assertEqual(json.loads((root / "out" / "prd.json").read_text())["document_id"], "PRD")
            self.assertEqual((root / "prd.md").read_text(encoding="utf-8"), self.prd)

    def test_missing_document_control_rejected(self):
        with self.assertRaisesRegex(module.ExtractionError, "Document Control"):
            module.extract_prd("# PRD\n\n#### PRD-FR-001\n")


if __name__ == "__main__":
    unittest.main()
