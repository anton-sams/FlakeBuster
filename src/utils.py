import json
import logging
from typing import Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def validate_logs(log_data: List[Dict]) -> bool:
    required_fields = {"test", "status", "time"}
    for entry in log_data:
        if not all(field in entry for field in required_fields):
            logger.error(f"Invalid log entry: {entry}")
            return False
    return True

def format_report(report: Dict[str, str]) -> str:
    if not report:
        return "No flaky tests detected."
    output = "Flaky Test Report:\n"
    for test, suggestion in report.items():
        output += f"- {test}: {suggestion}\n"
    return output

def save_json(data: Dict, filepath: str) -> None:
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        logger.info(f"Saved data to {filepath}")
    except Exception as e:
        logger.error(f"Failed to save JSON to {filepath}: {e}")