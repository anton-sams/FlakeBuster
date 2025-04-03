import requests
import json

def fetch_ci_logs(job_url, auth_token):
    response = requests.get(job_url, headers={"Authorization": f"Bearer {auth_token}"})
    logs = response.json()
    return [{"test": log["name"], "status": log["result"], "time": log["duration"]}
            for log in logs["tests"]]