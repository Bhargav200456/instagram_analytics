import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise Exception("OPENAI_API_KEY is missing in .env")

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_cluster_insight(cluster):
    """
    Generate ONE insight for the entire cluster.
    """

    cluster_name = cluster.get("cluster_name", "Unknown")

    posts = cluster.get("posts", [])

    if not posts:
        return "No posts available for this cluster."

    # Combine ALL posts in the cluster
    post_text = ""

    for index, post in enumerate(posts, start=1):

        caption = post.get("caption", "")
        hashtags = post.get("hashtags", [])

        if isinstance(hashtags, list):
            hashtags = " ".join(hashtags)

        post_text += f"""
Post {index}:
Caption: {caption}
Hashtags: {hashtags}
Content Type: {post.get("content_type", "")}
Date: {post.get("date", "")}
"""

    prompt = f"""
You are an Instagram content analyst.

Analyze the ENTIRE group of Instagram posts below as one cluster.

Cluster name:
{cluster_name}

Posts in this cluster:
{post_text}

Generate ONE concise insight for the entire cluster.

The insight should explain:
1. What the main theme/topic of the cluster is.
2. What common pattern exists across the posts.
3. What this could indicate about the content strategy or audience interest.

Do NOT give separate insights for individual posts.

Return only the final insight as a short paragraph.
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text