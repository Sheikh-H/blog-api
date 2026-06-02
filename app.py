from flask import Flask, jsonify, request
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from services.db import (
    add_post,
    delete_post,
    get_post,
    update_post,
    get_all,
    search_post,
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
        add_post(data)
        return {"Success": f"'{data['title']}' post added"}, 201
    except Exception as e:
        return {"Error": f"{e}"}, 500


@app.route("/posts/<int:_id>", methods=["DELETE"])
@limiter.limit("50 per hour")
def delete(_id):
    _id = int(_id)
    try:
        result = delete_post(_id)
        if result == True:
            return {"Success": "Post deleted"}, 204
        if result == False:
            return {"Error": "Unable to delete post"}, 404
    except Exception as e:
        return {"Error": f"{e}"}, 400


@app.route("/posts/<int:_id>", methods=["GET"])
@limiter.limit("50 per hour")
def get_one(_id):
    _id = int(_id)
    result = get_post(_id)
    if not result:
        return {"Error": "Post not found"}, 400
    return {
        "Succes": {
            "id": result["id"],
            "title": result["title"],
            "content": result["content"],
            "category": result["category"],
            "tags": result["tags"],
            "CreatedAt": result["createdAt"],
            "UpdatedAt": result["updatedAt"],
        }
    }, 200


@app.route("/posts/<int:_id>", methods=["PUT"])
@limiter.limit("50 per hour")
def update_one(_id):
    _id = int(_id)
    data = request.json
    result = update_post(_id, data)
    if result == True:
        return {"Success": "Post Updated!"}, 200
    elif result == "Not found":
        return {"Error": "Post not found"}, 404
    elif result == "Not Updated":
        return {"Error": "Unable to update"}, 400


@app.route("/posts", methods=["GET"])
@limiter.limit("50 per hour")
def get_posts():
    if not request.args.get("term"):
        data = get_all()
        if not data:
            return {"Error": "No posts found"}, 404
        return jsonify(data), 200
    else:
        term = request.args.get("term")
        result = search_post(term)
        if result:
            return jsonify(result), 200
        else:
            return {"Error": "Post not found"}, 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host="127.0.0.1")
