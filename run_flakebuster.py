from src.flake_detector import detect_flaky_tests
from src.mitigator import suggest_fixes

logs = "tests/test_logs.json"
flaky_tests = detect_flaky_tests(logs)
report = {test: suggest_fixes(test, pd.read_json(logs)) for test in flaky_tests}
with open("flake_report.json", "w") as f:
    json.dump(report, f, indent=2)