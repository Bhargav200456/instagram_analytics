from flask import Flask
from flask_cors import CORS

from routes.instagram import instagram_bp
from routes.insights import insights_bp


app = Flask(__name__)

CORS(app)


@app.route("/")
def home():

    return {
        "status": "success",
        "message": "Instagram Insight Backend Running"
    }


@app.route("/health")
def health():

    return {
        "status": "healthy"
    }


app.register_blueprint(
    instagram_bp,
    url_prefix="/api/instagram"
)


app.register_blueprint(
    insights_bp,
    url_prefix="/api/insights"
)


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )