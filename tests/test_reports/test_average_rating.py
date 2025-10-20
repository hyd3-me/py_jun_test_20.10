def test_average_rating_report_can_be_instantiated():
    """
    Test that AverageRatingReport can be created.
    This will fail if BaseReport is not implemented or if AverageRatingReport does not implement generate.
    """
    from src.reports.average_rating import AverageRatingReport

    report = AverageRatingReport()
    assert report is not None