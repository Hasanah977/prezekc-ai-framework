"""Cross-artifact checks for the synthetic P01-P06 acceptance fixture."""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "examples" / "acceptance"


class AcceptanceWorkflowTests(unittest.TestCase):
    def test_upstream_evidence_chain(self):
        system = (FIXTURES / "system-analysis.md").read_text(encoding="utf-8")
        research = (FIXTURES / "comparative-study.md").read_text(encoding="utf-8")
        analysis = (FIXTURES / "requirement-analysis.md").read_text(encoding="utf-8")
        prd = (FIXTURES / "prd.md").read_text(encoding="utf-8")
        self.assertIn("PROB-001", system)
        self.assertIn("SIM-OBS-001", research)
        self.assertIn("PROB-001", analysis)
        self.assertIn("NEED-001", analysis)
        self.assertIn("NEED-001", prd)
        self.assertIn("SIMULATED FIXTURE OWNER", prd)

    def test_design_references_match_registry_and_srs(self):
        design = (FIXTURES / "system-design.md").read_text(encoding="utf-8")
        srs = (FIXTURES / "srs.md").read_text(encoding="utf-8")
        registry = json.loads((FIXTURES / "design.json").read_text(encoding="utf-8"))
        registered = {row["id"] for row in registry["design_elements"]}
        referenced = set(re.findall(r"\bDES-\d{3,}\b", design))
        self.assertEqual(registered, referenced)
        for element in registry["design_elements"]:
            self.assertTrue(element["srs_ids"])
            for sid in element["srs_ids"]:
                self.assertIn(sid, srs)
                self.assertIn(sid, design)

    def test_simulation_not_marked_as_real_release(self):
        for name in ("system-analysis", "comparative-study", "requirement-analysis", "prd", "srs", "system-design"):
            content = (FIXTURES / f"{name}.md").read_text(encoding="utf-8").upper()
            self.assertTrue("SIMULAT" in content or "SYNTHETIC" in content, name)
        design = (FIXTURES / "system-design.md").read_text(encoding="utf-8")
        self.assertIn("NOT APPROVED FOR IMPLEMENTATION", design)


if __name__ == "__main__":
    unittest.main()
