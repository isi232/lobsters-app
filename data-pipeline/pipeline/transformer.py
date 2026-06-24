from datetime import datetime, timezone


def transform_post(raw_post_data: dict) -> dict:
    parsed = datetime.fromisoformat(raw_post_data["created_at"])
    created_utc = parsed.timestamp()

    return {
        "post_id":      raw_post_data["short_id"],
        "title":        raw_post_data["title"],
        "author": raw_post_data["submitter_user"],
        "score":        raw_post_data["score"],
        "num_comments": raw_post_data["comment_count"],
        "url":          raw_post_data["url"],
        "permalink":    raw_post_data["comments_url"],
        "created_utc":  created_utc,
        "fetched_at":   datetime.now(timezone.utc),
    }


def transform_posts(raw_json: list, limit: int = 10) -> list:
    return [transform_post(post) for post in raw_json[:limit]]
