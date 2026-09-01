from flask import Blueprint, request, jsonify

from services.instagram_service import get_instagram_posts
from services.clustering_service import cluster_posts
from services.insight_service import generate_cluster_insight


insights_bp = Blueprint("insights", __name__)


@insights_bp.route("/generate", methods=["GET"])
def generate_insights():

    username = request.args.get("username")

    if not username:
        return jsonify({
            "success": False,
            "message": "username is required"
        }), 400

    try:

        # -----------------------------------------
        # 1. Get Instagram posts
        # -----------------------------------------

        result = get_instagram_posts(username)

        raw_posts = []

        if isinstance(result, dict):

            outer_posts = result.get("posts")

            if isinstance(outer_posts, dict):
                raw_posts = outer_posts.get("posts", [])

            elif isinstance(outer_posts, list):
                raw_posts = outer_posts

        elif isinstance(result, list):

            for item in result:

                if isinstance(item, dict):

                    item_posts = item.get("posts", [])

                    if isinstance(item_posts, list):
                        raw_posts.extend(item_posts)

        # -----------------------------------------
        # 2. Clean posts
        # -----------------------------------------

        cleaned_posts = []

        for post in raw_posts:

            if not isinstance(post, dict):
                continue

            cleaned_posts.append({
                "id": post.get("id"),
                "username": username,
                "caption": post.get("caption", ""),
                "content_type": post.get("content_type"),
                "date": post.get("datetime"),
                "hashtags": post.get("post_hashtags") or [],
                "image_url": post.get("image_url"),
                "post_url": post.get("url")
            })

        if not cleaned_posts:

            return jsonify({
                "success": False,
                "message": "No Instagram posts found"
            }), 404

        # -----------------------------------------
        # 3. Create clusters
        # -----------------------------------------

        number_of_clusters = int(
            request.args.get("clusters", 3)
        )

        clusters = cluster_posts(
            cleaned_posts,
            number_of_clusters
        )

        # -----------------------------------------
        # 4. Generate ONE insight per cluster
        # -----------------------------------------

        results = []

        for cluster in clusters:

            insight = generate_cluster_insight(
                cluster
            )

            results.append({
                "cluster_id": cluster["cluster_id"],
                "cluster_name": cluster["cluster_name"],
                "post_count": cluster["post_count"],
                "insight": insight,
                "posts": cluster["posts"]
            })

        # -----------------------------------------
        # 5. Return final result
        # -----------------------------------------

        return jsonify({
            "success": True,
            "username": username,
            "total_posts": len(cleaned_posts),
            "total_clusters": len(results),
            "clusters": results
        })

    except ValueError:

        return jsonify({
            "success": False,
            "message": "clusters must be a number"
        }), 400

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500