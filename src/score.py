
from datetime import date

class Score:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    """
    def __init__(self, date: date) -> None:
        self.date = date
        self.hits = [True] * 25
    """