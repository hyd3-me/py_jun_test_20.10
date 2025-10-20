# src/reports/average_price.py

from typing import List, Dict
from collections import defaultdict
from tabulate import tabulate
from src.reports.base import BaseReport


class AveragePriceReport(BaseReport):
    def generate(self, data: List[Dict]) -> str:
        if not data:
            return tabulate([], headers=["Brand", "Average Price"], tablefmt="grid")

        prices_by_brand = defaultdict(list)

        for row in data:
            brand = row["brand"]
            price = float(row["price"])
            prices_by_brand[brand].append(price)

        avg_prices = {
            brand: round(sum(prices) / len(prices), 2)
            for brand, prices in prices_by_brand.items()
        }

        sorted_brands = sorted(avg_prices.items(), key=lambda x: x[1], reverse=True)

        table = [[name, avg] for name, avg in sorted_brands]
        headers = ["Brand", "Average Price"]
        return tabulate(table, headers=headers, tablefmt="grid", floatfmt=".2f")
