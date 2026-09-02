import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def _build_post_text(post):
    """
    Build searchable text from all useful fields available
    in an Instagram post.
    """

    parts = []

    caption = post.get("caption")
    if caption:
        parts.append(str(caption))

    hashtags = post.get("hashtags")
    if hashtags:
        if isinstance(hashtags, list):
            parts.extend(str(tag) for tag in hashtags)
        else:
            parts.append(str(hashtags))

    # Support alternative fields that may be returned
    # by different Instagram data providers.
    for field in [
        "description",
        "text",
        "title",
        "alt_text"
    ]:
        value = post.get(field)

        if value:
            parts.append(str(value))

    text = " ".join(parts)

    # Basic cleanup
    text = re.sub(r"\s+", " ", text).strip()

    return text


def cluster_posts(posts, number_of_clusters=3):
    """
    Cluster Instagram posts using TF-IDF + K-Means.

    The number of clusters is automatically reduced when
    there are not enough unique text representations.
    """

    if not posts:
        return []

    # --------------------------------
    # Build text for every post
    # --------------------------------

    documents = []

    for post in posts:
        documents.append(
            _build_post_text(post)
        )

    # --------------------------------
    # Check whether useful text exists
    # --------------------------------

    non_empty_documents = [
        text for text in documents
        if text
    ]

    # If there is no textual information,
    # return one cluster instead of forcing K-Means.
    if not non_empty_documents:

        return [{
            "cluster_id": 0,
            "cluster_name": "Instagram Posts",
            "post_count": len(posts),
            "posts": posts
        }]

    # --------------------------------
    # TF-IDF
    # --------------------------------

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=1000
    )

    try:
        X = vectorizer.fit_transform(documents)
    except ValueError:

        return [{
            "cluster_id": 0,
            "cluster_name": "Instagram Posts",
            "post_count": len(posts),
            "posts": posts
        }]

    # --------------------------------
    # Determine valid cluster count
    # --------------------------------

    unique_vectors = set()

    for row in X.toarray():
        unique_vectors.add(
            tuple(row)
        )

    unique_count = len(unique_vectors)

    actual_clusters = min(
        number_of_clusters,
        len(posts),
        unique_count
    )

    # K-Means needs at least 2 clusters
    # to actually perform clustering.
    if actual_clusters < 2:

        return [{
            "cluster_id": 0,
            "cluster_name": "Instagram Posts",
            "post_count": len(posts),
            "posts": posts
        }]

    # --------------------------------
    # K-Means
    # --------------------------------

    model = KMeans(
        n_clusters=actual_clusters,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X)

    # --------------------------------
    # Build clusters
    # --------------------------------

    clusters = []

    for cluster_id in range(actual_clusters):

        cluster_posts_list = []

        for index, label in enumerate(labels):

            if label == cluster_id:

                cluster_posts_list.append(
                    posts[index]
                )

        if not cluster_posts_list:
            continue

        clusters.append({
            "cluster_id": cluster_id,
            "cluster_name": f"Cluster {cluster_id + 1}",
            "post_count": len(cluster_posts_list),
            "posts": cluster_posts_list
        })

    return clusters