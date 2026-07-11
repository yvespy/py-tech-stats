import requests
from bs4 import BeautifulSoup

from config import BASE_URL, CATEGORY


class DouScraper:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": BASE_URL
        }

    def _get_csrf_token(self) -> None:
        self.session.get(BASE_URL, headers=self.headers)
        self.csrf_token = self.session.cookies.get("csrftoken")

    def _fetch_vacancies_page(self, count) -> dict:
        data = {
            "csrfmiddlewaretoken": self.csrf_token,
            "count": count
        }
        response = self.session.post(BASE_URL + "xhr-load/" + CATEGORY, data=data, headers=self.headers)
        return response.json()

    def _get_vacancy_urls(self, html):
        soup = BeautifulSoup(html, "html.parser")
        vacancy_url = soup.find_all("a", {"class": "vt"})

        return [link["href"] for link in vacancy_url]

    def _get_vacancy_description(self, url):
        response = self.session.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")
        description = soup.find("div", {"class": "vacancy-section"})

        return description.text

    def scrape_vacancies(self) -> dict:
        self._get_csrf_token()
        return self._fetch_vacancies_page(0)
