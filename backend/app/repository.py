from app.models import Post
from app.db import get_session

def get_top_posts(limit: int = 10) -> list:
    session = get_session()
    posts = (
        session.query(Post)
        .order_by(Post.score.desc())
        .limit(limit)
        .all()
    )
    session.close()
    return posts

def get_post_by_id(post_id: str):
    session = get_session()
    post = session.query(Post).filter_by(post_id=post_id).first()
    session.close()
    return post

def count_posts() -> int:
    session = get_session()
    count = session.query(Post).count()
    session.close()
    return count