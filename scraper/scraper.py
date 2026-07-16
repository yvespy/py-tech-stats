import json

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

    def _fetch_vacancies_page(self, count, exp: str = "") -> dict:
        data = {
            "csrfmiddlewaretoken": self.csrf_token,
            "count": count
        }
        url = BASE_URL + "xhr-load/" + CATEGORY
        if exp:
            url += f"&exp={exp}"
        response = self.session.post(url, data=data, headers=self.headers)
        return response.json()

    def scrape_vacancies(self) -> dict:
        self._get_csrf_token()
        return self._fetch_vacancies_page(0)

    def _get_vacancy_urls(self, html) -> list:
        soup = BeautifulSoup(html, "html.parser")
        vacancy_url = soup.find_all("a", {"class": "vt"})

        return [link["href"] for link in vacancy_url]

    def _get_vacancy_description(self, url) -> str:
        response = self.session.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")
        description = soup.find("div", {"class": "vacancy-section"})

        return description.get_text(separator=" ", strip=True).replace("\xa0", " ")

    def scrape_all(self, output_path: str, exp: str = "") -> None:
        self._get_csrf_token()

        offset = 0
        descriptions = []
        last_page = False

        while not last_page:
            page = self._fetch_vacancies_page(offset, exp)

            for url in self._get_vacancy_urls(page["html"]):
                descriptions.append(self._get_vacancy_description(url))

            last_page = page["last"]
            offset += 40

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(descriptions, file, ensure_ascii=False, indent=4)

        return None
