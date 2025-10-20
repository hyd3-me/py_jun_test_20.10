def test_report_manager_register_and_get():
    """
    Test that reports can be registered and retrieved by name.
    """
    from src.reports.manager import ReportManager
    from src.reports.average_rating import AverageRatingReport

    manager = ReportManager()
    report = AverageRatingReport()
    manager.register_report("average-rating", report)

    retrieved = manager.get_report("average-rating")
    assert retrieved is report
    assert isinstance(retrieved, AverageRatingReport)
