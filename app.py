from flask import Flask, jsonify, request
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from services.db import add_post

app = Flask(__name__)

limiter = Limiter(key_func=get_remote_address, app=app)


@app.route("/posts", methods=["POST"])
@limiter.limit("50 per hour")
def adding_post():
    data = request.json
    if (
        not data["title"]
        or not data["content"]
        or not data["category"]
        or not data["tags"]
    ):
        return {"Error": "Unable to add post, please use all required fields"}, 400
    try:
        add_post(data)
        return {"Success": f"{data['title']} post added"}, 201
    except Exception as e:
        return {"Error": f"{e}"}, 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host="127.0.0.1")
