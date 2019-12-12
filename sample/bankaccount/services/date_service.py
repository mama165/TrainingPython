from abc import ABC
from datetime import date


class DateService(ABC):
    def __init__(self):
        pass

    @staticmethod
    def get_date():
        return date.today()
