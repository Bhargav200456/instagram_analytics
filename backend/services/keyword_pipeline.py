from services.instagram_search import search_instagram
from services.instagram_keyword_service import (
    collect_instagram_posts
)


# --------------------------------------------------
# Helper functions
# --------------------------------------------------

def first_value(post, fields, default=None):
    """
    Return the first non-empty value found
    from a list of possible field names.
    """

    for field in fields:

        value = post.get(field)

        if value is not None and value != "":
            return value

    return default


def normalize_hashtags(value):
    """
    Convert different hashtag formats into a list.
    """

    if value is None:
        return []

    if isinstance(value, list):
        return value

    if isinstance(value, str):

        value = value.strip()

        if not value:
            return []

        if "," in value:

            return [
                item.strip()
                for item in value.split(",")
                if item.strip()
            ]

        return [
            item.strip()
            for item in value.split()
            if item.strip()
        ]

    return [str(value)]


# --------------------------------------------------
# Clean one Instagram post
# --------------------------------------------------

def clean_post(post, fallback_url=None):
    """
    Convert a Bright Data post into the common
    application format.
    """

    post_url = first_value(
        post,
        [
            "url",
            "post_url",
            "link",
            "permalink"
        ],
        fallback_url
    )

    post_id = first_value(
        post,
        [
            "id",
            "post_id",
            "shortcode",
            "short_code"
        ]
    )

    username = first_value(
        post,
        [
            "username",
            "user_name",
            "owner_username",
            "author_username"
        ]
    )

    caption = first_value(
        post,
        [
            "caption",
            "description",
            "text",
            "post_text"
        ],
        ""
    )

    content_type = first_value(
        post,
        [
            "content_type",
            "type",
            "post_type"
        ]
    )

    date = first_value(
        post,
        [
            "datetime",
            "date",
            "timestamp",
            "created_at",
            "posted_at"
        ]
    )

    hashtags = first_value(
        post,
        [
            "post_hashtags",
            "hashtags",
            "hash_tags"
        ],
        []
    )

    image_url = first_value(
        post,
        [
            "image_url",
            "thumbnail",
            "thumbnail_url",
            "display_url",
            "image"
        ]
    )

    return {
        "id": post_id,
        "username": username,
        "caption": str(caption) if caption else "",
        "content_type": content_type,
        "date": date,
        "hashtags": normalize_hashtags(
            hashtags
        ),
        "image_url": image_url,
        "post_url": post_url
    }


# --------------------------------------------------
# Main keyword pipeline
# --------------------------------------------------

def run_keyword_pipeline(
    keyword,
    max_results=5
):
    """
    Complete keyword-based Instagram pipeline.

    Keyword
        ↓
    SERP API
        ↓
    Instagram URLs
        ↓
    Bright Data
        ↓
    Clean posts
    """

    print("\n==============================")
    print("KEYWORD PIPELINE")
    print("==============================")

    print(
        "Keyword:",
        keyword
    )

    # --------------------------------------------------
    # STEP 1: Search Instagram
    # --------------------------------------------------

    print(
        "\n[1] Searching Instagram posts..."
    )

    urls = search_instagram(
        keyword,
        max_results=max_results
    )

    print(
        "Instagram URLs found:",
        len(urls)
    )

    if not urls:

        return {
            "keyword": keyword,
            "urls": [],
            "posts": []
        }

    # --------------------------------------------------
    # STEP 2: Collect posts
    # --------------------------------------------------

    print(
        "\n[2] Collecting Instagram post data..."
    )

    posts = collect_instagram_posts(
        urls
    )

    print(
        "Posts collected:",
        len(posts)
    )

    # --------------------------------------------------
    # STEP 3: Clean posts
    # --------------------------------------------------

    print(
        "\n[3] Cleaning post data..."
    )

    cleaned_posts = []

    for index, post in enumerate(posts):

        if not isinstance(post, dict):
            continue

        fallback_url = None

        if index < len(urls):
            fallback_url = urls[index]

        cleaned_post = clean_post(
            post,
            fallback_url
        )

        cleaned_posts.append(
            cleaned_post
        )

    print(
        "Cleaned posts:",
        len(cleaned_posts)
    )

    # --------------------------------------------------
    # Count available text
    # --------------------------------------------------

    posts_with_text = 0

    for post in cleaned_posts:

        caption = post.get(
            "caption",
            ""
        )

        hashtags = post.get(
            "hashtags",
            []
        )

        if caption or hashtags:
            posts_with_text += 1

    print(
        "Posts with text:",
        posts_with_text
    )

    return {
        "keyword": keyword,
        "urls": urls,
        "posts": cleaned_posts
    }