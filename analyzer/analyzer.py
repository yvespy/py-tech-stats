import json
from collections import Counter

import pandas as pd
from textblob import TextBlob

from config import NON_TECH_WORDS


class TechAnalyzer:
    def __init__(self, filepath):
        self.df = self._load_data(filepath)

    def _load_data(self, filepath) -> pd.DataFrame:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        df = pd.DataFrame(data, columns=["description"])
        return df

    def _process_text(self):
        tokens = self.df["description"].apply(
            lambda x: [word for word, tag in TextBlob(x).tags if tag == "NNP" and word not in NON_TECH_WORDS]
        )
        return tokens

    def get_top_technologies(self, n=20):
        words = self._process_text()

        counter = Counter()

        for vacancy in words:
            unique_words = {
                word
                for word in vacancy
                if word.isalpha() and len(word) > 2 and word.isascii()
            }

            counter.update(unique_words)
        return counter.most_common(n)
