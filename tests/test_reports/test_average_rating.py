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