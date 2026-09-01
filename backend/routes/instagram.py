from flask import Blueprint, request, jsonify

from services.instagram_service import get_instagram_posts
from services.clustering_service import cluster_posts


instagram_bp = Blueprint("instagram", __name__)


@instagram_bp.route("/posts", methods=["GET"])
def get_posts():

    username = request.args.get("username")

    if not username:
        return jsonify({
            "success": False,
            "message": "username is required"
        }), 400

    try:

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

        return jsonify({
            "success": True,
            "username": username,
            "total_posts": len(cleaned_posts),
            "posts": cleaned_posts
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@instagram_bp.route("/cluster", methods=["GET"])
def get_clusters():

    username = request.args.get("username")

    if not username:
        return jsonify({
            "success": False,
            "message": "username is required"
        }), 400

    try:

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

        # Get number of clusters from request
        number_of_clusters = int(
            request.args.get("clusters", 3)
        )

        clusters = cluster_posts(
            cleaned_posts,
            number_of_clusters
        )

        return jsonify({
            "success": True,
            "username": username,
            "total_posts": len(cleaned_posts),
            "total_clusters": len(clusters),
            "clusters": clusters
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