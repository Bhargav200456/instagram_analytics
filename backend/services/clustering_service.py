import re

from openai import OpenAI
from dotenv import load_dotenv
import os

from sklearn.cluster import KMeans


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


def clean_text(text):
    """
    Clean caption or hashtag text.
    """

    if not text:
        return ""

    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove mentions
    text = re.sub(r"@\w+", "", text)

    # Remove hashtag symbol
    text = text.replace("#", " ")

    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def create_embedding(text):
    """
    Convert text into a semantic embedding using OpenAI.
    """

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding


def cluster_posts(posts, number_of_clusters=3):
    """
    Group Instagram posts based on semantic meaning.
    """

    if not posts:
        return []

    # ------------------------------------------------
    # Create text for every post
    # ------------------------------------------------

    documents = []

    for post in posts:

        caption = post.get("caption", "")

        hashtags = post.get("hashtags", [])

        if isinstance(hashtags, list):
            hashtags_text = " ".join(hashtags)
        else:
            hashtags_text = str(hashtags)

        combined_text = f"{caption} {hashtags_text}"

        documents.append(
            clean_text(combined_text)
        )

    # ------------------------------------------------
    # Handle one post
    # ------------------------------------------------

    if len(posts) == 1:

        return [{
            "cluster_id": 0,
            "cluster_name": "General",
            "post_count": 1,
            "posts": posts
        }]

    # ------------------------------------------------
    # Create semantic embeddings
    # ------------------------------------------------

    embeddings = []

    for document in documents:

        if not document:
            document = "Instagram post"

        embedding = create_embedding(document)

        embeddings.append(embedding)

    # ------------------------------------------------
    # Make sure cluster count is valid
    # ------------------------------------------------

    number_of_clusters = min(
        number_of_clusters,
        len(posts)
    )

    # ------------------------------------------------
    # K-Means clustering
    # ------------------------------------------------

    model = KMeans(
        n_clusters=number_of_clusters,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(embeddings)

    # ------------------------------------------------
    # Create clusters
    # ------------------------------------------------

    clusters = {}

    for index, label in enumerate(labels):

        if label not in clusters:
            clusters[label] = []

        clusters[label].append(
            posts[index]
        )

    # ------------------------------------------------
    # Format result
    # ------------------------------------------------

    result = []

    for cluster_id, cluster_posts_list in clusters.items():

        cluster_name = generate_cluster_name(
            cluster_posts_list
        )

        result.append({
            "cluster_id": int(cluster_id),
            "cluster_name": cluster_name,
            "post_count": len(cluster_posts_list),
            "posts": cluster_posts_list
        })

    return result


def generate_cluster_name(posts):
    """
    Generate a meaningful name for a cluster.
    """

    text_parts = []

    for post in posts:

        caption = post.get("caption", "")

        hashtags = post.get("hashtags", [])

        if isinstance(hashtags, list):
            hashtags = " ".join(hashtags)

        text_parts.append(
            f"{caption} {hashtags}"
        )

    combined_text = "\n".join(text_parts)

    # Ask OpenAI to name the cluster
    prompt = f"""
You are an Instagram content analyst.

Below are several Instagram posts that belong to
the same semantic cluster.

Posts:

{combined_text}

Give this cluster a short and meaningful topic name.

Examples:

Messi Jersey
Wildlife Conservation
Space Exploration
Travel Destinations
Football Content
Fashion Trends

Return ONLY the cluster name.
Do not explain it.
Keep it between 2 and 5 words.
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    name = response.output_text.strip()

    return name