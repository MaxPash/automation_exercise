from dotenv import load_dotenv
import os

load_dotenv()

URLS = {
    "prod": "https://www.automationexercise.com/",
    "stage": "https://stage.automationexercise.com/",
    "qa": "https://qa.automationexercise.com/",
    "dev": "https://dev.automationexercise.com/",
}

def get_url():
    env = os.getenv('TEST_ENV', "qa").lower()

    try:
        return URLS[env]
    except KeyError:
        raise ValueError(f"Unsupported environment: {env}")

