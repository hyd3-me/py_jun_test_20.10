# tests/conftest.py

import pytest
from pathlib import Path


@pytest.fixture
def sample_products_csv_files(tmp_path):
    """
    Create temporary CSV files with sample product data for testing.
    Returns a list of file paths.
    """
    # Create first CSV file
    file1 = tmp_path / "products1.csv"
    file1.write_text("name,brand,price,rating\n" "iPhone 15,apple,999,4.9\n")

    # Create second CSV file
    file2 = tmp_path / "products2.csv"
    file2.write_text("name,brand,price,rating\n" "Galaxy S23,samsung,1199,4.8\n")

    return [file1, file2]
