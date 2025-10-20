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


def test_main_unknown_report(monkeypatch, tmp_path, capsys):
    """
    Test that main.py prints an error when an unknown report is requested.
    """
    from src.main import main

    # Create a temporary CSV file
    file1 = tmp_path / "products.csv"
    file1.write_text("name,brand,price,rating\n" "iPhone 15,apple,999,4.9\n")

    # Mock command line arguments with unknown report
    monkeypatch.setattr(
        "sys.argv", ["main.py", "--files", str(file1), "--report", "unknown-report"]
    )

    # Run main
    main()

    # Capture output
    captured = capsys.readouterr()

    # Check that error message is printed
    assert "Unknown report: unknown-report" in captured.err


def test_main_empty_csv_files(monkeypatch, tmp_path, capsys):
    """
    Test that main.py handles empty CSV files correctly.
    """
    from src.main import main

    # Create empty CSV files
    file1 = tmp_path / "empty1.csv"
    file1.write_text("name,brand,price,rating\n")

    file2 = tmp_path / "empty2.csv"
    file2.write_text("name,brand,price,rating\n")

    # Mock command line arguments
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--files", str(file1), str(file2), "--report", "average-rating"],
    )

    # Run main
    main()

    # Capture output
    captured = capsys.readouterr()

    # Check that the report is empty but valid
    output = captured.out
    assert "Brand" in output
    assert "Average Rating" in output
    # Should only contain header and separators, no data rows
    lines = output.strip().split("\n")
    assert len([line for line in lines if "|" in line]) == 1  # Header only


def test_main_multiple_files_integration(monkeypatch, tmp_path, capsys):
    """
    Test that main.py correctly processes multiple CSV files and calculates average ratings.
    """
    from src.main import main

    # Create first CSV file
    file1 = tmp_path / "file1.csv"
    file1.write_text(
        "name,brand,price,rating\n"
        "iPhone 15,apple,999,4.9\n"
        "iPhone 12,apple,599,4.5\n"
    )

    # Create second CSV file
    file2 = tmp_path / "file2.csv"
    file2.write_text(
        "name,brand,price,rating\n"
        "Galaxy S23,samsung,1199,4.8\n"
        "Galaxy A52,samsung,399,4.4\n"
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

    output = captured.out

    # Check that both brands are present
    assert "apple" in output
    assert "samsung" in output

    # Check that apple has average: (4.9 + 4.5) / 2 = 4.70
    assert "4.70" in output

    # Check that samsung has average: (4.8 + 4.4) / 2 = 4.60
    assert "4.60" in output

    # Check sorting: apple (4.70) should come before samsung (4.60)
    lines = output.strip().split("\n")
    brand_lines = [line for line in lines if "apple" in line or "samsung" in line]
    assert "apple" in brand_lines[0]
    assert "samsung" in brand_lines[1]
