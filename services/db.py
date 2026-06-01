from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime
from flask import jsonify

load_dotenv()

client = MongoClient(os.environ.get("MONGO_URI"))
db = client["blog"]
table = db["posts"]


def add_post(title=None, content=None, category=None, tags=None):
    if not title or not content or not category or not tags:
        return {
            "Error": "Enter title, content, category and tags fields to add post"
        }, 400
    post = {
        'title':title,
        'content':content,
        'category':category,
        'tags': [tag for tag in tags]
    }