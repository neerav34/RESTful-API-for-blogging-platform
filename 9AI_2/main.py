from fastapi import FastAPI, HTTPException
from models import Post, Comment, LikeDislike
from database import BlogDatabase

app = FastAPI()

db = BlogDatabase("mongodb://localhost:27017/", "blog_database")


@app.post("/posts/", response_model=str)
async def create_post(post: Post):
    post_id = db.create_post(post)
    return post_id


@app.get("/posts/", response_model=list[Post])
async def read_posts():
    return db.read_posts()


@app.get("/posts/{post_id}", response_model=Post)
async def read_post(post_id: str):
    post = db.read_post(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.put("/posts/{post_id}", response_model=bool)
async def update_post(post_id: str, post: Post):
    if not db.read_post(post_id):
        raise HTTPException(status_code=404, detail="Post not found")
    return db.update_post(post_id, post)


@app.delete("/posts/{post_id}", response_model=bool)
async def delete_post(post_id: str):
    if not db.read_post(post_id):
        raise HTTPException(status_code=404, detail="Post not found")
    return db.delete_post(post_id)


@app.post("/posts/{post_id}/comments/", response_model=str)
async def create_comment(post_id: str, comment: Comment):
    post = db.read_post(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    post.comments.append(comment)
    db.update_post(post_id, post)
    return "Comment added successfully"


@app.post("/posts/{post_id}/likes/", response_model=bool)
async def like_post(post_id: str, like: LikeDislike):
    post = db.read_post(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    post.likes += like.value
    db.update_post(post_id, post)
    return True


@app.post("/posts/{post_id}/dislikes/", response_model=bool)
async def dislike_post(post_id: str, dislike: LikeDislike):
    post = db.read_post(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    post.dislikes += dislike.value
    db.update_post(post_id, post)
    return True
