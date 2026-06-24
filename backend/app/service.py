from app import repository

def get_top_posts_for_api(limit: int = 10) -> dict:
    if limit < 1: limit = 1
    if limit > 50: limit = 50
    posts = repository.get_top_posts(limit)
    posts_data = [post.to_dict() for post in posts]
    return {"success": True, "data": posts_data, "count": len(posts_data)}

def get_single_post_for_api(post_id: str) -> dict:
    post = repository.get_post_by_id(post_id)
    if post is None:
        return {"success": False, "error": "Post not found."}
    return {"success": True, "data": post.to_dict()}

def get_stats_for_api() -> dict:
    count = repository.count_posts()
    return {"success": True, "data": {"total_posts": count}}