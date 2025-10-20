# src/parsers/csv_parser.py

from pathlib import Path
from typing import List, Dict
import csv


def read_csv_files(file_paths: List[Path]) -> List[Dict]:
    """
    Read and combine data from multiple CSV files.
    Each row is returned as a dictionary.
    """
    combined_data = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            combined_data.extend(reader)
    return combined_data