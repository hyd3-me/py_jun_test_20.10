import pytest


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


def test_parse_args_missing_files(monkeypatch):
    """
    Test that an error occurs when --files argument is missing.
    """
    monkeypatch.setattr("sys.argv", ["main.py", "--report", "average-rating"])

    from src.cli import parse_args

    with pytest.raises(SystemExit):
        parse_args()


def test_parse_args_missing_report(monkeypatch):
    """
    Test that an error occurs when --report argument is missing.
    """
    monkeypatch.setattr("sys.argv", ["main.py", "--files", "products1.csv"])

    from src.cli import parse_args

    with pytest.raises(SystemExit):
        parse_args()


def test_parse_args_file_not_found(monkeypatch, tmp_path):
    """
    Test that an error occurs when one of the files does not exist.
    """
    nonexistent_file = tmp_path / "nonexistent.csv"

    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--files", str(nonexistent_file), "--report", "average-rating"],
    )

    from src.cli import parse_args

    with pytest.raises(SystemExit):
        parse_args()
