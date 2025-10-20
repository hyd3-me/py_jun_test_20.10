# src/reports/average_rating.py

from src.reports.base import BaseReport
from typing import List, Dict


class AverageRatingReport(BaseReport):
    def generate(self,  data: List[Dict]) -> str:
        return "Placeholder"