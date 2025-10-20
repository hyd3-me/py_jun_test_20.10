def test_parse_args_success(monkeypatch, tmp_path):
    """
    Test that valid --files and --report arguments are parsed correctly.
    """
    # Create a temporary CSV file for testing
    file1 = tmp_path / "products1.csv"
    file1.write_text("name,brand,price,rating\n")

    # Mock sys.argv to simulate command line input
    monkeypatch.setattr(
        "sys.argv", ["main.py", "--files", str(file1), "--report", "average-rating"]
    )

    # Import here to avoid side effects during test collection
    from src.cli import parse_args

    args = parse_args()
    assert len(args.files) == 1
    assert str(args.files[0]) == str(file1)
    assert args.report == "average-rating"
