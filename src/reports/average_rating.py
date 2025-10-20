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

def test_average_rating_report_single_product_per_brand():
    """
    Test that average rating is correct when each brand has only one product.
    """
    from src.reports.average_rating import AverageRatingReport

    data = [
        {"name": "iPhone 15", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "Galaxy S23", "brand": "samsung", "price": "1199", "rating": "4.8"},
    ]

    report = AverageRatingReport()
    result = report.generate(data)

    assert "apple" in result
    assert "samsung" in result
    # Each brand has only one product, so average = rating
    assert "4.90" in result  # apple
    assert "4.80" in result  # samsung