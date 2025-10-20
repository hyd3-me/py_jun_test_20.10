def test_read_csv_files_success(sample_products_csv_files):
    """
    Test that CSV files are read and combined correctly.
    """
    from src.parsers.csv_parser import read_csv_files

    # Use fixture to get the file paths
    file_paths = sample_products_csv_files

    result = read_csv_files(file_paths)

    assert len(result) == 2
    assert result[0]["name"] == "iPhone 15"
    assert result[0]["brand"] == "apple"
    assert result[1]["name"] == "Galaxy S23"
    assert result[1]["brand"] == "samsung"


def test_read_csv_files_empty_file(tmp_path):
    """
    Test that reading an empty CSV file (with headers only) returns an empty list.
    """
    from src.parsers.csv_parser import read_csv_files

    # Create an empty CSV file with headers
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("name,brand,price,rating\n")  # Only headers

    result = read_csv_files([empty_file])

    assert result == []


def test_read_csv_files_multiple_files_with_same_brand(tmp_path):
    """
    Test that data from multiple files with the same brand is combined correctly.
    """
    from src.parsers.csv_parser import read_csv_files

    # Create first CSV file
    file1 = tmp_path / "products1.csv"
    file1.write_text("name,brand,price,rating\n" "iPhone 15,apple,999,4.9\n")

    # Create second CSV file
    file2 = tmp_path / "products2.csv"
    file2.write_text(
        "name,brand,price,rating\n"
        "iPhone 12,apple,599,4.5\n"
        "Galaxy S23,samsung,1199,4.8\n"
    )

    result = read_csv_files([file1, file2])

    assert len(result) == 3
    apple_items = [item for item in result if item["brand"] == "apple"]
    samsung_items = [item for item in result if item["brand"] == "samsung"]

    assert len(apple_items) == 2
    assert len(samsung_items) == 1
    assert apple_items[0]["name"] == "iPhone 15"
    assert apple_items[1]["name"] == "iPhone 12"
    assert samsung_items[0]["name"] == "Galaxy S23"
