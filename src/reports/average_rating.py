# src/reports/average_rating.py

from typing import List, Dict
from collections import defaultdict
from tabulate import tabulate
from src.reports.base import BaseReport


class AverageRatingReport(BaseReport):
    def generate(self, data: List[Dict]) -> str:
        headers = ["Brand", "Average Rating"]
        if not data:
            return tabulate([], headers=headers, tablefmt="grid")

        ratings_by_brand = defaultdict(list)

        for row in data:
            brand = row['brand']
            rating = float(row['rating'])
            ratings_by_brand[brand].append(rating)

        avg_ratings = {
            brand: round(sum(ratings) / len(ratings), 2)
            for brand, ratings in ratings_by_brand.items()
        }

        sorted_brands = sorted(avg_ratings.items(), key=lambda x: x[1], reverse=True)

        table = [[name, avg] for name, avg in sorted_brands]
        return tabulate(table, headers=headers, tablefmt="grid", floatfmt=".2f")
