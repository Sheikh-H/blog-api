from flask import Flask, jsonify, request
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from services.db import add_post

app = Flask(__name__)

limiter = Limiter(key_func=get_remote_address, app=app)


@app.route("/", methods=["POST"])
@limiter.limit("50 per hour")
def adding_post():
    data = request.json()
    add_post(data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host="127.0.0.1")
