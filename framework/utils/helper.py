import json
import os
import time


def load_signup_data(key):

    path = "../data/test_signup_data.json"

    json_path = os.path.join(os.path.dirname(__file__), path)

    with open(json_path, 'r') as file:
        data = json.load(file)

    return data[key]

def generate_email():
    timestamp = int(time.time())
    return f"test_{timestamp}@test.test"