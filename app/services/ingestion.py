import json
import os
from google_play_scraper import app as fetch_app

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "apps_sample.json")

def load_apps():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Data file not found: {DATA_PATH}")

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def fetch_playstore_app(package_name):
    data = fetch_app(package_name)

    return {
        "name": data["title"],
        "package": package_name,
        "developer": data["developer"],
        "developer_email": data.get("developerEmail", ""),
        "permissions": data.get("permissions", []),
        "description": data.get("description", "")
    }