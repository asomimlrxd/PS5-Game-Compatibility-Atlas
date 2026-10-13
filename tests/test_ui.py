import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BeginnerFriendlyUITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.app = (ROOT / "app.js").read_text(encoding="utf-8")
        cls.css = (ROOT / "styles.css").read_text(encoding="utf-8")

    def test_advanced_filters_are_collapsed_by_default(self):
        block = self.html.split('<details class="advanced-filters">', 1)[1].split("</details>", 1)[0]
        self.assertNotIn(" open", block)
        self.assertIn('data-i18n="advancedFilters"', block)

    def test_game_reports_are_progressively_disclosed(self):
        self.assertIn('class="report-details"', self.app)
        self.assertIn("viewReports", self.app)
        self.assertIn("aggregateHelp", self.app)

    def test_plain_language_translations_exist(self):
        for phrase in ("Queres saber se um jogo funciona?", "Find your game", "Há relatos positivos", "There are positive reports"):
            self.assertIn(phrase, self.app)

    def test_accessible_readable_styles_exist(self):
        self.assertIn(".search-help", self.css)
        self.assertIn(".report-details > summary", self.css)
        self.assertIn("font-size: 15px", self.css)
        self.assertIn(".results-grid.single-result", self.css)


if __name__ == "__main__":
    unittest.main()
