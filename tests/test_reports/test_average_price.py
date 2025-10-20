def test_average_price_report_single_brand():
    """
    Test that average price is calculated correctly for a single brand with multiple products.
    """
    from src.reports.average_price import AveragePriceReport

    data = [
        {"name": "iPhone 15", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "iPhone 12", "brand": "apple", "price": "599", "rating": "4.5"},
    ]

    report = AveragePriceReport()
    result = report.generate(data)

    assert "apple" in result
    assert "799.00" in result  # (999 + 599) / 2 = 799.00
