from flask import Flask, jsonify, request
from flask_cors import CORS
from app import service

app = Flask(__name__)
CORS(app)

@app.route("/api/posts/top", methods=["GET"])
def get_top_posts():
    limit = request.args.get("limit", default=10, type=int)
    result = service.get_top_posts_for_api(limit)
    return jsonify(result)

@app.route("/api/posts/<string:post_id>", methods=["GET"])
def get_post(post_id):
    result = service.get_single_post_for_api(post_id)
    if not result["success"]:
        return jsonify(result), 404
    return jsonify(result), 200

@app.route("/api/stats", methods=["GET"])
def get_stats():
    result = service.get_stats_for_api()
    return jsonify(result)

@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"success": True, "message": "API is running."}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)