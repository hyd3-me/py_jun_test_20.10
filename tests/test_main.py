def test_main_integration(monkeypatch, tmp_path, capsys):
    """
    Test that main.py correctly processes CSV files and generates a report.
    """
    from src.main import main

    # Create sample CSV files
    file1 = tmp_path / "products1.csv"
    file1.write_text("name,brand,price,rating\n" "iPhone 15,apple,999,4.9\n")

    file2 = tmp_path / "products2.csv"
    file2.write_text(
        "name,brand,price,rating\n"
        "Galaxy S23,samsung,1199,4.8\n"
        "iPhone 12,apple,599,4.5\n"
    )

    # Mock command line arguments
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--files", str(file1), str(file2), "--report", "average-rating"],
    )

    # Run main
    main()

    # Capture output
    captured = capsys.readouterr()

    # Check that the report contains expected data
    output = captured.out
    assert "apple" in output
    assert "samsung" in output
    assert "4.70" in output  # Average for apple: (4.9 + 4.5) / 2 = 4.70
