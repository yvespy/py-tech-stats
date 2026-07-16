import os
from datetime import datetime

from config import DATE_FORMAT, RAW_DATA_DIR, CHARTS_DIR


class OutputFiles:
    def __init__(self, experience: str):
        self.experience = experience
        self.current_date = datetime.now().strftime(DATE_FORMAT)

    @property
    def json_path(self):
        return os.path.join(
            RAW_DATA_DIR,
            f"{self.current_date}_{self.experience}.json"
        )

    @property
    def chart_path(self):
        return os.path.join(
            CHARTS_DIR,
            f"{self.current_date}_{self.experience}.png"
        )
