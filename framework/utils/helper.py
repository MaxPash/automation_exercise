import json
import os
import time
from pathlib import Path


def load_signup_data(key):
    path = "../data/test_signup_data.json"
    json_path = os.path.join(os.path.dirname(__file__), path)
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data[key]


def load_signup_payload() -> dict:
    """Загрузить весь JSON с данными для регистрации."""
    json_path = Path(__file__).resolve().parent.parent / "data" / "test_signup_data.json"
    with json_path.open(encoding="utf-8") as f:
        return json.load(f)


def generate_email():
    timestamp = int(time.time())
    return f"test_{timestamp}@test.test"