from pymongo import MongoClient
from bson import ObjectId
from models import Post


class BlogDatabase:
    def __init__(self, url: str, db_name: str):
        self.client = MongoClient(url)
        self.db = self.client[db_name]
        self.collection = self.db["posts"]

    def create_post(self, post: Post) -> str:
        post_id = self.collection.insert_one(post.dict()).inserted_id
        return str(post_id)

    def read_posts(self) -> list[Post]:
        posts = self.collection.find()
        return [Post(**post) for post in posts]

    def read_post(self, post_id: str) -> Post:
        post = self.collection.find_one({"_id": ObjectId(post_id)})
        if post:
            return Post(**post)
        return None

    def update_post(self, post_id: str, post: Post) -> bool:
        updated_post = self.collection.find_one_and_update(
            {"_id": ObjectId(post_id)}, {"$set": post.dict()}, return_document=True
        )
        return True if updated_post else False

    def delete_post(self, post_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(post_id)})
        return True if result.deleted_count else False
