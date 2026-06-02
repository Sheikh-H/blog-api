from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime
from flask import jsonify

load_dotenv()

client = MongoClient(os.environ.get("MONGO_URI"))
db = client["rdmpsh-blog"]
table = db["blog-posts"]


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


def get_post(_id):
    post = table.find_one(
        {"id": _id},
        {
            "_id": 0,
            "id": 1,
            "title": 1,
            "content": 1,
            "category": 1,
            "tags": 1,
            "createdAt": 1,
            "updatedAt": 1,
        },
    )
    if post:
        list(post)
        return post
    else:
        return None


def delete_post(_id):
    result = table.find_one_and_delete({"id": _id})
    if result:
        return True
    else:
        return None


def update_post(_id, key, value):
    now = f"{datetime.now().replace(microsecond=0)}"
    post = table.find_one({"id": _id})
    if not post:
        return "not found"
    else:
        try:
            table.find_one_and_update(
                {"id": _id}, {"$set": {key: value, "updatedAt": now}}
            )
            return "updated"
        except:
            return "unable to update"


def get_posts():
    posts = table.find(
        {},
        {
            "_id": 0,
            "id": 1,
            "title": 1,
            "content": 1,
            "category": 1,
            "tags": 1,
            "createdAt": 1,
            "updatedAt": 1,
        },
    )
    if posts:
        posts = list(posts)
        return posts
    else:
        return None


def search_posts(term):
    posts = table.find(
        {
            "$or": [
                {"title": {"$regex": str(term), "$options": "i"}},
                {"tags": {"$regex": str(term), "$options": "i"}},
                {"category": {"$regex": str(term), "$options": "i"}},
            ]
        },
        {
            "_id": 0,
            "id": 1,
            "title": 1,
            "content": 1,
            "category": 1,
            "tags": 1,
            "createdAt": 1,
            "updatedAt": 1,
        },
    )
    if posts:
        posts = list(posts)
        return posts
    else:
        return None
