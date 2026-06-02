from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from services.db import (
    add_post,
    get_post,
    delete_post,
    update_post,
    get_posts,
    search_posts,
)

app = Flask(__name__)

limiter = Limiter(key_func=get_remote_address, app=app)


@app.route("/posts", methods=["POST"])
@limiter.limit("50 per hour")
def add():
    data = request.json
    if not data.get("title"):
        return {"Error": "Unable to add post, please use all required fields"}, 400
    if not data.get("content"):
        return {"Error": "Unable to add post, please use all required fields"}, 400
    if not data.get("category"):
        return {"Error": "Unable to add post, please use all required fields"}, 400
    if not data.get("tags"):
        return {"Error": "Unable to add post, please use all required fields"}, 400
    try:
        post = add_post(data)
        return jsonify(post), 201
    except Exception as e:
        return {"Error": f"{e}"}, 500


@app.route("/posts/<int:_id>", methods=["GET"])
@limiter.limit("50 per hour")
def fetch_post(_id):
    _id = int(_id)
    post = get_post(_id)
    if post:
        return jsonify(post), 200
    else:
        return {"Error": "Post not found"}, 404


@app.route("/posts", methods=["GET"])
@limiter.limit("50 per hour")
def posts():
    term = request.args.get("term")
    if not term:
        posts = get_posts()
        if posts:
            return jsonify(posts), 200
        else:
            return {"Error": "No posts"}, 404
    else:
        searched = search_posts(term)
        if searched:
            return jsonify(searched), 200
        else:
            return {"error": "search result null"}, 404


@app.route("/posts/<int:_id>", methods=["DELETE"])
@limiter.limit("50 per hour")
def delete(_id):
    _id = int(_id)
    try:
        result = delete_post(_id)
        if result:
            return "", 204
        else:
            return {"Error": "Unable to delete post"}, 404
    except:
        return {"Error": "Unable to delete post"}, 404


@app.route("/posts/<int:_id>", methods=["PUT"])
def update(_id):
    _id = int(_id)
    post = request.json
    for key, value in post.items():
        if key not in ["title", "content", "category", "tags"]:
            return {"error": "unable to update"}, 400
    for key, value in post.items():
        result = update_post(_id, key, value)
    if result:
        return jsonify(result), 200
    elif result == "not found":
        return {"error": "post not found"}, 404
    elif result == "unable to update":
        return {"error": "Unable to update"}, 400
