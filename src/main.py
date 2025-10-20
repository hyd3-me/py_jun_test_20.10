# src/main.py

import sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", force=True)
logger = logging.getLogger(__name__)

sys.path.append(str(Path(__file__).resolve().parent))

from cli import parse_args
from parsers.csv_parser import read_csv_files
from reports.manager import ReportManager
from reports.average_rating import AverageRatingReport
from reports.average_price import AveragePriceReport


def main():
    args = parse_args()

    # Read all CSV files
    data = read_csv_files(args.files)

    # Setup report manager
    manager = ReportManager()
    manager.register_report("average-rating", AverageRatingReport())
    manager.register_report("average-price", AveragePriceReport())

    # Get and generate report
    report = manager.get_report(args.report)
    if report is None:
        logger.error(f"Unknown report: {args.report}")
        return

    result = report.generate(data)
    print(result)


if __name__ == "__main__":
    main()
