from flask import Blueprint, request, jsonify

from services.keyword_pipeline import run_keyword_pipeline
from services.clustering_service import cluster_posts
from services.insight_service import generate_cluster_insight


insights_bp = Blueprint("insights", __name__)


@insights_bp.route("/search", methods=["GET"])
def search_keyword():
    """
    Keyword-based Instagram analytics pipeline.

    Keyword
        ↓
    Instagram search
        ↓
    Bright Data post collection
        ↓
    Clustering
        ↓
    AI insight generation
    """

    keyword = request.args.get("keyword")

    if not keyword:
        return jsonify({
            "success": False,
            "message": "keyword is required"
        }), 400

    try:

        # --------------------------------
        # STEP 1: Keyword → Instagram posts
        # --------------------------------

        pipeline_result = run_keyword_pipeline(
            keyword,
            max_results=5
        )

        cleaned_posts = pipeline_result["posts"]

        if not cleaned_posts:
            return jsonify({
                "success": False,
                "message": "No Instagram posts found",
                "keyword": keyword
            }), 404

        # --------------------------------
        # STEP 2: Clustering
        # --------------------------------

        number_of_clusters = int(
            request.args.get("clusters", 3)
        )

        clusters = cluster_posts(
            cleaned_posts,
            number_of_clusters
        )

        # --------------------------------
        # STEP 3: AI insight for each cluster
        # --------------------------------

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

        # --------------------------------
        # FINAL RESPONSE
        # --------------------------------

        return jsonify({
            "success": True,
            "keyword": keyword,
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