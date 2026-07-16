# Python Tech Market Analyzer

A Python application that scrapes Python vacancies from **DOU**, analyzes job descriptions, and generates charts showing
the most in-demand technologies on the market.

## Features

* Scrapes public Python vacancies from DOU.
* Supports different experience levels:

    * All
    * Junior / Trainee
    * Middle
    * Senior
    * Senior+
* Saves raw vacancy descriptions as JSON files.
* Analyzes technology mentions using **TextBlob** and custom filtering.
* Counts each technology only once per vacancy to avoid duplicate mentions.
* Generates charts with the most demanded technologies using Matplotlib.
* Clean project architecture following the **Single Responsibility Principle (SRP)**.

---

## Project Structure

```text
py-tech-stats/
│
├── analyzer/
│   └── analyzer.py
│
├── scraper/
│   └── scraper.py
│
├── visualizer/
│   └── chart_builder.py
│
├── utils/
│   └── file_utils.py
│
├── data/
│   ├── raw/
│   └── charts/
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies

* Python 3.12+
* Requests
* BeautifulSoup4
* Pandas
* TextBlob
* Matplotlib

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yvespy/py-tech-stats.git
cd py-tech-stats
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download the required TextBlob corpora:

```bash
python -m textblob.download_corpora
```

---

## Usage

Run the application:

```bash
python main.py
```

The application will:

1. Scrape Python vacancies from DOU.
2. Save raw vacancy descriptions as JSON.
3. Analyze the extracted technologies.
4. Generate charts with the most frequently mentioned technologies.

---

## Output Example

### Raw data

```text
data/raw/
├── 2026-07-15_all.json
├── 2026-07-15_junior-trainee.json
├── 2026-07-15_middle.json
├── 2026-07-15_senior.json
└── 2026-07-15_senior+.json
```

### Charts

```text
data/charts/
├── 2026-07-15_all.png
├── 2026-07-15_junior-trainee.png
├── 2026-07-15_middle.png
├── 2026-07-15_senior.png
└── 2026-07-15_senior+.png
```

---

## Configuration

Most project settings can be configured in `config.py`, including:

* Vacancy category
* Experience levels
* Output directories
* Date format
* List of excluded non-technology words

---

## Project Architecture

The application is divided into independent modules:

* **Scraper** — downloads vacancies and saves raw data.
* **Analyzer** — extracts and counts technologies.
* **Visualizer** — generates charts.
* **Utils** — helper classes for file management.

This separation makes the project easier to maintain and extend.

---

## Notes

* The scraper only collects **publicly available** information.
* No authentication is required.
* The project is intended for educational purposes.

---

## Limitations

This project identifies technologies using TextBlob named entity tagging together with custom filtering rules.

While this approach provides good results for most vacancies, it is not perfect. Some technology names may be missed,
while a few non-technology words may occasionally appear in the final statistics.

To improve the results, a manually maintained exclusion list (`NON_TECH_WORDS`) is used. However, due to the variety of
writing styles across job descriptions, achieving 100% accurate technology extraction without a dedicated NLP model or
predefined technology database is difficult.