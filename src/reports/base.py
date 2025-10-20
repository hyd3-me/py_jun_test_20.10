# src/reports/base.py

from abc import ABC, abstractmethod
from typing import List, Dict


class BaseReport(ABC):
    """
    Abstract base class for all reports.
    """

    @abstractmethod
    def generate(self,  data: List[Dict]) -> str:
        """
        Generate report as a string from input data.
        """
        pass