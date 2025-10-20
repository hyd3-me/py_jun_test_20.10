# src/reports/manager.py

from typing import Dict
from src.reports.base import BaseReport


class ReportManager:
    """
    Manages available reports and allows to retrieve them by name.
    """

    def __init__(self):
        self.reports: Dict[str, BaseReport] = {}

    def register_report(self, name: str, report: BaseReport):
        """
        Register a report under a given name.
        """
        self.reports[name] = report

    def get_report(self, name: str) -> BaseReport:
        """
        Get a report instance by name.
        """
        return self.reports.get(name)
