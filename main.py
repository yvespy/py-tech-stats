from config import EXPERIENCE_LEVEL
from scraper.scraper import DouScraper
from analyzer.analyzer import TechAnalyzer
from utils.file_utils import OutputFiles
from visualizer.chart_builder import build_chart

if __name__ == "__main__":
    scraper = DouScraper()

    for level, exp in EXPERIENCE_LEVEL.items():
        files = OutputFiles(level)

        # Scrape and save to JSON
        scraper.scrape_all(files.json_path, exp)

        # Reading JSON and parsing
        analyzer = TechAnalyzer(files.json_path)
        data = analyzer.get_top_technologies()

        # Build a chart
        build_chart(data, files.chart_path)
