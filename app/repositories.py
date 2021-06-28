import pdb

from fastapi import HTTPException

from app.models import User, Post, PostResume
from app.permissions import is_authenticated
from app.schemas import UserUpdateSchema, PostUpdateSchema, PostResumeUpdateSchema


@is_authenticated(str)
def retrieve_users(token):
    return User.objects()


@is_authenticated(str)
def retrieve_user(token, user_id):
    user = User.objects(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@is_authenticated(str)
def create_user(token, user_schema: UserUpdateSchema):
    user = User(
        name=user_schema.name,
        title=user_schema.title,
        address=user_schema.address
    )
    user.save_social(user_schema.social_networks)
    user.save()
    return user


@is_authenticated(str)
def update_user(token, user_id, user_schema: UserUpdateSchema):
    user = User.objects(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = user_schema.name
    user.title = user_schema.title
    user.address = user_schema.address
    user.save_social(user_schema.social_networks)
    user.save()
    return user


@is_authenticated(str)
def remove_user(token, user_id):
    user = User.objects(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.delete()


def retrieve_post_resume(token, post_id):
    post = PostResume.objects(id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@is_authenticated(str)
def create_post_resume(token, post: PostResumeUpdateSchema):
    m_post = PostResume(
        lang=post.lang,
        title=post.title,
        subtitle=post.subtitle,
        description=post.description,
        company_image=post.company_image,
        begin_date=post.begin_date,
        end_date=post.end_date
    )
    m_post.save()
    return m_post


@is_authenticated(str)
def update_post_resume(token, post_id, post: PostResumeUpdateSchema):
    m_post = PostResume.objects(id=post_id)
    if m_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    m_post.lang = post.lang
    m_post.title = post.title
    m_post.subtitle = post.subtitle
    m_post.description = post.description
    m_post.company_image = post.company_image
    m_post.begin_date = post.begin_date
    m_post.end_date = post.end_date
    m_post.save()
    return m_post


@is_authenticated(str)
def remove_post_resume(token, post_id):
    m_post = PostResume.objects(id=post_id)
    if m_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    m_post.delete()


def retrieve_post(token, post_id):
    post = Post.objects(id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@is_authenticated(str)
def create_post(token, post: PostUpdateSchema):
    m_post = Post(
        lang=post.lang,
        title=post.title,
        subtitle=post.subtitle,
        description=post.description
    )
    m_post.save()
    return m_post


@is_authenticated(str)
def update_post(token, post_id, post: PostUpdateSchema):
    m_post = Post.objects(id=post_id)
    if m_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    m_post.lang = post.lang
    m_post.title = post.title
    m_post.subtitle = post.subtitle
    m_post.description = post.description
    m_post.save()
    return m_post


@is_authenticated(str)
def remove_post(token, post_id):
    m_post = Post.objects(id=post_id)
    if m_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    m_post.delete()
