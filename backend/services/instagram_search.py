import os
import requests
from dotenv import load_dotenv

load_dotenv()

BRIGHTDATA_API_KEY = os.getenv("BRIGHTDATA_API_KEY")
BRIGHTDATA_SERP_ZONE = os.getenv("BRIGHTDATA_SERP_ZONE")

SERP_API_URL = "https://api.brightdata.com/request"


def search_instagram(keyword, max_results=10):
    """
    Search Google for Instagram posts related to a keyword
    using Bright Data SERP API.
    """

    if not BRIGHTDATA_API_KEY:
        raise Exception("BRIGHTDATA_API_KEY is missing in .env")

    if not BRIGHTDATA_SERP_ZONE:
        raise Exception("BRIGHTDATA_SERP_ZONE is missing in .env")

    query = f'site:instagram.com/p/ "{keyword}"'

    google_url = (
        "https://www.google.com/search?q="
        + requests.utils.quote(query)
        + "&hl=en&gl=us"
    )

    headers = {
        "Authorization": f"Bearer {BRIGHTDATA_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "zone": BRIGHTDATA_SERP_ZONE,
        "url": google_url,
        "format": "raw",
        "data_format": "parsed_light"
    }

    response = requests.post(
        SERP_API_URL,
        headers=headers,
        json=payload,
        timeout=60
    )

    print("SERP API Status:", response.status_code)

    if response.status_code != 200:
        raise Exception(
            f"SERP API error: "
            f"{response.status_code} - {response.text}"
        )

    data = response.json()

    organic_results = data.get("organic", [])

    print("Organic results:", len(organic_results))

    instagram_urls = []

    for result in organic_results:

        if not isinstance(result, dict):
            continue

        link = result.get("link", "")

        if "instagram.com/p/" in link:
            instagram_urls.append(link)

        if len(instagram_urls) >= max_results:
            break

    return instagram_urls