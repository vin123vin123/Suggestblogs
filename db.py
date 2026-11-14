from datetime import datetime
from bson.binary import Binary
import pymongo
import streamlit as st


@st.cache_resource
def get_collection():
    # Works whether st.secrets["mongo"] is a direct string or a [mongo] uri section
    mongo_secret = st.secrets["mongo"]
    uri = (
        mongo_secret["uri"] if isinstance(mongo_secret, dict) else mongo_secret
    )
    client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
    db = client.blogdb
    return db.posts


@st.cache_data(ttl=60)
def get_all_posts():
    collection = get_collection()
    return list(collection.find().sort("created_at", -1))


def create_post(title, author, content, image_bytes=None, image_type=None):
    collection = get_collection()
    doc = {
        "title": title,
        "author": author,
        "content": content,
        "image": Binary(image_bytes) if image_bytes else None,
        "image_type": image_type,
        "created_at": datetime.now().isoformat(),
    }
    collection.insert_one(doc)
    get_all_posts.clear()
