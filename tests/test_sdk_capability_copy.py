import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CapabilityCopyTests(unittest.TestCase):
    def test_odcs_wrapper_command_and_boundary_are_public(self):
        expected = (
            "open-data-products product wrap-contract --input contract.yaml "
            "--output product.yaml"
        )
        for filename in ("index.html", "docs/reference.html", "llms.txt"):
            content = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn(expected, content, filename)
            self.assertIn("validated ODPS 4.2 draft", content, filename)

    def test_contract_intelligence_command_report_and_review_boundary_are_public(self):
        expected = (
            "open-data-products portfolio discover-contracts ./contracts "
            "--output ./portfolio-discovery --json"
        )
        for filename in ("index.html", "docs/reference.html", "llms.txt"):
            content = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn(expected, content, filename)
            self.assertIn("offline HTML report", content, filename)
            self.assertIn("does not automatically create or approve data products", content, filename)
