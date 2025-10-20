def test_average_rating_report_can_be_instantiated():
    """
    Test that AverageRatingReport can be created.
    This will fail if BaseReport is not implemented or if AverageRatingReport does not implement generate.
    """
    from src.reports.average_rating import AverageRatingReport

    report = AverageRatingReport()
    assert report is not None

def test_average_rating_report_single_brand():
    """
    Test that average rating is calculated correctly for a single brand with multiple products.
    """
    from src.reports.average_rating import AverageRatingReport

    data = [
        {"name": "iPhone 15", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "iPhone 12", "brand": "apple", "price": "599", "rating": "4.5"},
    ]

    report = AverageRatingReport()
    result = report.generate(data)

    assert "apple" in result
    assert "4.70" in result  # (4.9 + 4.5) / 2 = 4.70

def test_average_rating_report_multiple_brands():
    """
    Test that multiple brands are sorted by average rating descending.
    """
    from src.reports.average_rating import AverageRatingReport

    data = [
        {"name": "iPhone 15", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "Galaxy S23", "brand": "samsung", "price": "1199", "rating": "4.8"},
        {"name": "Redmi Note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    ]

    report = AverageRatingReport()
    result = report.generate(data)

    # Check that all brands are present
    assert "apple" in result
    assert "samsung" in result
    assert "xiaomi" in result

    # Check sorting: apple (4.9) > samsung (4.8) > xiaomi (4.6)
    lines = result.strip().split('\n')
    brand_lines = [line for line in lines if 'apple' in line or 'samsung' in line or 'xiaomi' in line]

    # The order should be: apple, samsung, xiaomi
    assert brand_lines[0].count('apple') == 1
    assert brand_lines[1].count('samsung') == 1
    assert brand_lines[2].count('xiaomi') == 1

def test_average_rating_report_empty_data():
    """
    Test that an empty data list returns an empty table.
    """
    from src.reports.average_rating import AverageRatingReport

    report = AverageRatingReport()
    result = report.generate([])

    assert "Brand" in result
    assert "Average Rating" in result
    # Should only contain header and separators, no data rows
    lines = result.strip().split('\n')
    assert len([line for line in lines if '|' in line]) == 1  # Header only

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

def test_average_rating_report_rounding():
    """
    Test that average ratings are rounded to 2 decimal places.
    Example: (4.9 + 4.8 + 4.7) / 3 = 4.800... -> should appear as 4.80.
    """
    from src.reports.average_rating import AverageRatingReport

    data = [
        {"name": "iPhone 15", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "iPhone 12", "brand": "apple", "price": "599", "rating": "4.8"},
        {"name": "iPhone 11", "brand": "apple", "price": "499", "rating": "4.7"},
    ]

    report = AverageRatingReport()
    result = report.generate(data)

    assert "apple" in result
    # Average: (4.9 + 4.8 + 4.7) / 3 = 4.8
    assert "4.80" in result  # Check rounding to 2 decimal places