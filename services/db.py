from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime
from flask import jsonify

load_dotenv()

client = MongoClient(os.environ.get("MONGO_URI"))
db = client["blog"]
table = db["posts"]


def add_post(data):
    now = f"{datetime.now().replace(microsecond=0)}"
    last_post = table.find_one(sort=[("id", -1)])
    _id = 1 if not last_post else last_post["id"] + 1
    new_post = {
        "id": _id,
        "title": data["title"],
        "content": data["content"],
        "category": data["category"],
        "tags": data["tags"],
        "createdAt": now,
        "updatedAt": "Null",
    }
    table.insert_one(new_post)
    return True


def delete_post(_id):
    try:
        table.delete_one({"id": _id})
        return True
    except Exception as e:
        print(e)
        return False


def get_post(_id):
    post = table.find_one({"id": _id})
    if post:
        return post
    if not post:
        return None


def update_post(_id, data):
    post = table.find_one({"id": _id})
    if not post:
        return False
    else:
        if data.get("content"):
            table.find_one_and_update({"id": _id}, {"content": data["content"]})
            return True
        elif data.get("title"):
            table.find_one_and_update({"id": _id}, {"title": data["title"]})
            return True
        elif data.get("category"):
            table.find_one_and_update({"id": _id}, {"category": data["category"]})
            return True
        elif data.get("tags"):
            table.find_one_and_update({"id": _id}, {"tags": data["tags"]})
            return True
        else:
            
