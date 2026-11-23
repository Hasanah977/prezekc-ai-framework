"""Unit tests for the requirements traceability validator."""

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "validate_requirements.py"
spec = importlib.util.spec_from_file_location("validate_requirements", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def fixtures():
    prd = {
        "document_id": "PRD", "version": "1.0", "status": "APPROVED",
        "approval": {"approved_by": "Project Owner", "decision_reference": "DEC-001"},
        "requirements": [{"id": "PRD-FR-001", "priority": "MUST"}],
    }
    srs = {
        "document_id": "SRS", "version": "1.0", "status": "APPROVED",
        "source_prd_version": "1.0",
        "requirements": [{"id": "SRS-FR-001.1", "parent_requirements": ["PRD-FR-001"]}],
    }
    rtm = {
        "document_id": "RTM", "version": "1.0", "source_prd_version": "1.0",
        "source_srs_version": "1.0",
        "mappings": [{"prd_id": "PRD-FR-001", "srs_id": "SRS-FR-001.1"}],
    }
    return prd, srs, rtm


class RequirementsValidatorTests(unittest.TestCase):
    def test_valid_baseline(self):
        self.assertEqual(validator.validate(*fixtures()), ([], []))

    def test_unapproved_prd(self):
        prd, srs, rtm = fixtures()
        prd["status"] = "DRAFT"
        errors, _ = validator.validate(prd, srs, rtm)
        self.assertTrue(any("approved baseline" in error for error in errors))

    def test_missing_mandatory_coverage(self):
        prd, srs, rtm = fixtures()
        srs["requirements"] = []
        rtm["mappings"] = []
        errors, _ = validator.validate(prd, srs, rtm)
        self.assertTrue(any("no SRS coverage" in error for error in errors))

    def test_invalid_parent_reference(self):
        prd, srs, rtm = fixtures()
        srs["requirements"][0]["parent_requirements"] = ["PRD-FR-999"]
        errors, _ = validator.validate(prd, srs, rtm)
        self.assertTrue(any("unknown parent" in error for error in errors))

    def test_duplicate_requirement_id(self):
        prd, srs, rtm = fixtures()
        prd["requirements"].append({"id": "PRD-FR-001", "priority": "SHOULD"})
        errors, _ = validator.validate(prd, srs, rtm)
        self.assertTrue(any("duplicate ID" in error for error in errors))

    def test_missing_reverse_mapping(self):
        prd, srs, rtm = fixtures()
        rtm["mappings"] = []
        errors, _ = validator.validate(prd, srs, rtm)
        self.assertTrue(any("missing mapping" in error for error in errors))

    def test_unverified_design_reference(self):
        prd, srs, rtm = fixtures()
        rtm["mappings"][0]["design_ids"] = ["DES-001"]
        errors, _ = validator.validate(prd, srs, rtm)
        self.assertTrue(any("cannot be verified" in error for error in errors))

    def test_verified_design_and_test_references(self):
        prd, srs, rtm = fixtures()
        rtm["mappings"][0]["design_ids"] = ["DES-001"]
        rtm["mappings"][0]["test_ids"] = ["TC-001"]
        errors, warnings = validator.validate(
            prd, srs, rtm,
            design={"design_elements": [{"id": "DES-001"}]},
            tests={"test_cases": [{"id": "TC-001"}]},
        )
        self.assertEqual((errors, warnings), ([], []))

    def test_mismatched_source_baseline(self):
        prd, srs, rtm = fixtures()
        srs["source_prd_version"] = "0.9"
        errors, _ = validator.validate(prd, srs, rtm)
        self.assertTrue(any("does not match" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
