from pipeline.models import Post
from pipeline.db import get_session


def load_posts(posts: list) -> dict:
    session = get_session()
    inserted = 0
    updated = 0

    for post in posts:
        existing = session.query(Post).filter_by(post_id=post["post_id"]).first()

        if existing:
            existing.score = post["score"]
            existing.num_comments = post["num_comments"]
            updated += 1
        else:
            new_post = Post(
                post_id=post["post_id"],
                title=post["title"],
                author=post["author"],
                score=post["score"],
                num_comments=post["num_comments"],
                url=post["url"],
                permalink=post["permalink"],
                created_utc=post["created_utc"],
                fetched_at=post["fetched_at"],
            )
            session.add(new_post)
            inserted += 1

    session.commit()
    session.close()

    return {"inserted": inserted, "updated": updated, "total": len(posts)}
