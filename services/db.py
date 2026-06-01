from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime
from flask import jsonify, request
import requests

load_dotenv()

client = MongoClient(os.environ.get("MONGO_URI"))
db = client["blog"]
table = db["posts"]


def add_post(data):
    now = str(datetime.now().replace(microsecond=0))
    if (
        not data["title"]
        or not data["content"]
        or not data["category"]
        or not data["tags"]
    ):
        return {"Error": "Unable to add post, please use all required fields"}, 400

    new_post = {
        "title": data["title"],
        "content": data["content"],
        "category": data["category"],
        "tags": data["tags"],
        "createdAt": now,
        "updatedAt": None,
    }
    try:
        table.insert_one(new_post)
        return {"Success": f"{data['title']} post added!"}, 201
    except Exception as e:
        return {"Error": "{e}"}, 400
