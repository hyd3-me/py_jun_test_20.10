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