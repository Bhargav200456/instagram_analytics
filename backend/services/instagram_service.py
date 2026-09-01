import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

BRIGHTDATA_API_KEY = os.getenv("BRIGHTDATA_API_KEY")

SCRAPE_URL = "https://api.brightdata.com/datasets/v3/scrape"

DATASET_ID = "gd_l1vikfch901nx3by4"

HEADERS = {
    "Authorization": f"Bearer {BRIGHTDATA_API_KEY}",
    "Content-Type": "application/json"
}


def get_instagram_posts(username):
    """
    Start Bright Data Instagram post collection
    and wait until the snapshot is ready.
    """

    if not BRIGHTDATA_API_KEY:
        raise Exception("BRIGHTDATA_API_KEY is missing in .env")

    payload = {
        "input": [
            {
                "user_name": username
            }
        ]
    }

    params = {
        "dataset_id": DATASET_ID,
        "type": "discover_new",
        "discover_by": "user_name",
        "include_errors": "true"
    }

    # 1. Start the scraper
    response = requests.post(
        SCRAPE_URL,
        params=params,
        headers=HEADERS,
        json=payload,
        timeout=120
    )

    if response.status_code not in [200, 202]:
        raise Exception(
            f"Bright Data API error: "
            f"{response.status_code} - {response.text}"
        )

    result = response.json()

    snapshot_id = result.get("snapshot_id")

    if not snapshot_id:
        return result

    # 2. Wait for the snapshot
    download_url = (
        f"https://api.brightdata.com/datasets/v3/snapshot/"
        f"{snapshot_id}"
    )

    for _ in range(30):

        status_response = requests.get(
            download_url,
            headers={
                "Authorization": f"Bearer {BRIGHTDATA_API_KEY}"
            },
            timeout=60
        )

        if status_response.status_code == 200:

            return status_response.json()

        if status_response.status_code in [202, 404]:

            time.sleep(5)
            continue

        raise Exception(
            f"Bright Data snapshot error: "
            f"{status_response.status_code} - "
            f"{status_response.text}"
        )

    raise Exception(
        "Bright Data scraper is taking too long to complete."
    )