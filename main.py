from scraper.scraper import DouScraper
from analyzer.analyzer import TechAnalyzer
from utils.file_utils import OutputFiles
from visualizer.chart_builder import build_chart

files = OutputFiles("all")

# Scrape and save to JSON
scraper = DouScraper()
scraper.scrape_all(files.json_path)

# Reading JSON and parsing
analyzer = TechAnalyzer(files.json_path)
data = analyzer.get_top_technologies()

# Build a chart
build_chart(data, files.chart_path)
