import pdb
from typing import List

import uvicorn
from fastapi import FastAPI

from app.models import Post, PostResume
from app.repositories import (
    create_user, update_user, remove_user, retrieve_users, retrieve_user, retrieve_post,
    create_post, update_post, remove_post, remove_post_resume, update_post_resume,
    create_post_resume, retrieve_post_resume
)
from app.schemas import (
    UserRetrieveSchema, UserUpdateSchema, PostRetrieveSchema, PostUpdateSchema,
    PostResumeUpdateSchema, PostResumeRetrieveSchema
)

app = FastAPI()


@app.get("/")
def root():
    return "hello world!"


@app.get("/users", response_model=List[UserRetrieveSchema])
def all_users(token):
    users = retrieve_users(token=token)
    pdb.set_trace()
    return users


@app.get("/user/{user_id}", response_model=UserRetrieveSchema)
def get_user(token, user_id):
    user = retrieve_user(token=token, user_id=user_id)
    return user


@app.post("/user", response_model=UserRetrieveSchema)
def post_user(token: str, user_schema: UserUpdateSchema):
    user = create_user(token=token, user_schema=user_schema)
    return user


@app.put("/user/{user_id}", response_model=UserRetrieveSchema)
def put_user(token: str, user_id, user_schema: UserUpdateSchema):
    user = update_user(token=token, user_id=user_id, user_schema=user_schema)
    return user


@app.delete("/user/{user_id}")
def delete_user(token: str, user_id: int):
    remove_user(token=token, user_id=user_id)
    return {"message": "User removed."}


@app.get("/posts", response_model=List[PostRetrieveSchema])
def all_posts():
    posts = Post.objects(id=1).first()
    return posts


@app.get("/post/{post_id}", response_model=PostRetrieveSchema)
def get_post(post_id):
    post = retrieve_post(post_id=post_id)
    return post


@app.post("/post", response_model=PostRetrieveSchema)
def save_post(token, post: PostUpdateSchema):
    post = create_post(token=token, post=post)
    return post


@app.put("/post/{post_id}", response_model=PostRetrieveSchema)
def put_post(token, post_id, post: PostUpdateSchema):
    post = update_post(token=token, post_id=post_id, post=post)
    return post


@app.delete("/post/{post_id}")
def delete_post(token, post_id):
    remove_post(token=token, post_id=post_id)
    return {"message": "Post deletado"}


@app.get("/posts-resume", response_model=List[PostResumeRetrieveSchema])
def all_posts():
    return PostResume.objects()


@app.get("/post-resume/{post_id}", response_model=PostResumeRetrieveSchema)
def get_post_resume(post_id):
    post = retrieve_post_resume(post_id=post_id)
    return post


@app.post("/post-resume", response_model=PostResumeRetrieveSchema)
def save_post_resume(token, post: PostResumeUpdateSchema):
    post = create_post_resume(token=token, post=post)
    return post


@app.put("/post-resume/{post_id}", response_model=PostResumeRetrieveSchema)
def put_post_resume(token, post_id, post: PostResumeUpdateSchema):
    post = update_post_resume(token=token, post_id=post_id, post=post)
    return post


@app.delete("/post-resume/{post_id}")
def delete_post_resume(token, post_id):
    remove_post_resume(token=token, post_id=post_id)
    return {"message": "Post resume deletado"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
