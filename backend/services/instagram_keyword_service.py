import os
import time
import json
import requests
from dotenv import load_dotenv


# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

ENV_FILE = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_FILE)


BRIGHTDATA_API_KEY = os.getenv(
    "BRIGHTDATA_API_KEY"
)


# --------------------------------------------------
# Bright Data configuration
# --------------------------------------------------

DATASET_ID = "gd_lk5ns7kz21pck8jpis"

TRIGGER_URL = (
    "https://api.brightdata.com/datasets/v3/trigger"
)

PROGRESS_URL = (
    "https://api.brightdata.com/datasets/v3/progress"
)

SNAPSHOT_URL = (
    "https://api.brightdata.com/datasets/v3/snapshot"
)


# --------------------------------------------------
# Collect Instagram posts
# --------------------------------------------------

def collect_instagram_posts(urls):
    """
    Collect Instagram post data from Instagram URLs
    using Bright Data's Collect Posts by URL dataset.
    """

    if not BRIGHTDATA_API_KEY:
        raise Exception(
            "BRIGHTDATA_API_KEY is missing in .env"
        )

    if not urls:
        return []

    headers = {
        "Authorization": (
            f"Bearer {BRIGHTDATA_API_KEY}"
        ),
        "Content-Type": "application/json"
    }

    # --------------------------------------------------
    # Prepare input
    # --------------------------------------------------

    payload = [
        {
            "url": url
        }
        for url in urls
    ]

    print("\nSending URLs to Bright Data...")

    # --------------------------------------------------
    # STEP 1: Trigger dataset
    # --------------------------------------------------

    response = requests.post(
        f"{TRIGGER_URL}?dataset_id={DATASET_ID}",
        headers=headers,
        json=payload,
        timeout=60
    )

    print(
        "Instagram scraper status:",
        response.status_code
    )

    if response.status_code not in [200, 201]:
        raise Exception(
            "Instagram scraper error: "
            f"{response.status_code} - "
            f"{response.text}"
        )

    data = response.json()

    snapshot_id = data.get("snapshot_id")

    if not snapshot_id:
        raise Exception(
            f"No snapshot_id returned: {data}"
        )

    print(
        "Snapshot ID:",
        snapshot_id
    )

    # --------------------------------------------------
    # STEP 2: Wait for completion
    # --------------------------------------------------

    for attempt in range(30):

        time.sleep(5)

        progress_response = requests.get(
            f"{PROGRESS_URL}/{snapshot_id}",
            headers={
                "Authorization":
                f"Bearer {BRIGHTDATA_API_KEY}"
            },
            timeout=30
        )

        if progress_response.status_code != 200:

            print(
                "Could not check progress:",
                progress_response.status_code
            )

            continue

        progress_data = (
            progress_response.json()
        )

        status = progress_data.get("status")

        print(
            f"Attempt {attempt + 1}: "
            f"status = {status}"
        )

        if status == "ready":
            break

        if status in [
            "failed",
            "error"
        ]:
            raise Exception(
                "Instagram scraping failed: "
                f"{progress_data}"
            )

    else:

        raise Exception(
            "Instagram scraping timed out"
        )

    # --------------------------------------------------
    # STEP 3: Download results
    # --------------------------------------------------

    print(
        "\nDownloading scraped data..."
    )

    download_response = requests.get(
        f"{SNAPSHOT_URL}/{snapshot_id}",
        headers={
            "Authorization":
            f"Bearer {BRIGHTDATA_API_KEY}"
        },
        timeout=60
    )

    print(
        "Download status:",
        download_response.status_code
    )

    if download_response.status_code != 200:

        raise Exception(
            "Failed to download results: "
            f"{download_response.status_code} - "
            f"{download_response.text}"
        )

    # --------------------------------------------------
    # STEP 4: Parse JSONL
    # --------------------------------------------------

    text = download_response.text.strip()

    if not text:
        return []

    posts = []

    lines = text.splitlines()

    print(
        "Result lines received:",
        len(lines)
    )

    for line in lines:

        line = line.strip()

        if not line:
            continue

        try:

            post = json.loads(line)

            if isinstance(post, dict):
                posts.append(post)

        except json.JSONDecodeError:

            print(
                "Warning: Could not parse "
                "result line"
            )

    return posts