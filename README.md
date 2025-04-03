# FlakeBuster

A tool to detect and mitigate flaky tests in QA automation suites, built for the Kyiv QA Automation Summit 2025 Hackathon.

## Overview
FlakeBuster analyzes test execution logs to identify flaky tests using metrics like failure frequency and execution time variability. It leverages a Random Forest Classifier for prediction and suggests actionable fixes, making test suites more reliable.

## Prerequisites
- Python 3.9+
- Git

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd FlakeBuster

## Install dependencies:
```bash

pip install -r requirements.txt
```
(Optional) Generate sample logs:
```bash

pytest tests/sample_tests.py --json-report --json-report-file=tests/test_logs.json
```
## Usage
Run FlakeBuster with a test log file:
```bash

python run_flakebuster.py --logs tests/test_logs.json
```
Output: A flake_report.json file and console summary of flaky tests and suggestions.

## Example Output

Flaky Test Report:
- test_api_call_flaky: Investigate race conditions in test_api_call_flaky.
- test_database_flaky: Add retry logic for test_database_flaky due to unstable execution time.

Integration with CI/CD
Provide a Jenkins job URL and API token:
```bash

python run_flakebuster.py --ci-url <jenkins-job-url> --token <api-token>
```
Files:

src/flake_detector.py: Detects flaky tests.

src/data_collector.py: Fetches logs from CI/CD.

src/mitigator.py: Suggests fixes.

src/utils.py: Helper functions.

tests/sample_tests.py: Sample test suite.

tests/test_logs.json: Sample log data.

