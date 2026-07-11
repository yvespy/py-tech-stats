import os

BASE_URL = "https://jobs.dou.ua/vacancies/"
DATE_FORMAT = "%Y-%m-%d"

EXPERIENCE_LEVEL = {
    "junior/trainee": "0-1",
    "middle": "1-3",
    "senior": "3-5",
    "senior+": "5plus"
}

CATEGORY = "?category=Python"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw") + "/"
CHARTS_DIR = os.path.join(BASE_DIR, "data", "charts") + "/"
