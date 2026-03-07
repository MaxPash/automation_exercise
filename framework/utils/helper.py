import json
import os
import time
import uuid
from pathlib import Path


def load_signup_data(key):
    path = "../data/test_signup_data.json"
    json_path = os.path.join(os.path.dirname(__file__), path)
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data[key]


def load_signup_payload() -> dict:
    """Load all JSON with data for registration."""
    json_path = Path(__file__).resolve().parent.parent / "data" / "test_signup_data.json"
    with json_path.open(encoding="utf-8") as f:
        return json.load(f)


def generate_email():
    timestamp = int(time.time())
    unique_id = uuid.uuid4().hex[:8]
    return f"test_user_{timestamp}_{unique_id}@test.test"