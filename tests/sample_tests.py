import time
import random
import pytest

def test_login_stable():
    assert True

def test_api_call_flaky():
    time.sleep(random.uniform(0.1, 0.5))
    assert random.choice([True, False])  # 50% chance of failure

def test_database_flaky():
    sleep_time = random.uniform(0.2, 1.0)
    time.sleep(sleep_time)
    assert sleep_time < 0.8  # Fails if sleep exceeds 0.8s

def test_logout_stable():
    time.sleep(0.1)
    assert True