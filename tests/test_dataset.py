import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


class AtlasDatasetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((DATA_DIR / "atlas-data.json").read_text(encoding="utf-8"))
        js_text = (DATA_DIR / "atlas-data.js").read_text(encoding="utf-8").strip()
        prefix = "window.ATLAS_DATA = "
        if not js_text.startswith(prefix) or not js_text.endswith(";"):
            raise AssertionError("atlas-data.js must define window.ATLAS_DATA as JSON.")
        cls.js_data = json.loads(js_text[len(prefix):-1])

    def test_json_and_javascript_data_match(self):
        self.assertEqual(self.data, self.js_data)

    def test_project_version_is_current(self):
        self.assertEqual(self.data["meta"].get("version"), "0.3.0")
        self.assertEqual(self.data["meta"].get("application_version"), "0.3.0")

    def test_report_ids_are_unique(self):
        ids = [row["id"] for row in self.data["reports"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(ids), 80)

    def test_sources_have_urls(self):
        self.assertTrue(self.data["sources"])
        self.assertTrue(all(str(source.get("url", "")).startswith("https://") for source in self.data["sources"]))

    def test_csv_matches_report_count(self):
        with (DATA_DIR / "atlas-reports.csv").open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), len(self.data["reports"]))


if __name__ == "__main__":
    unittest.main()
