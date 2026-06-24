import requests

USER_AGENT = "python:lobsters-top-posts-student-project:v1.0 (by /u/your_username_here)"
LOBSTERS_HOTTEST_URL = "https://lobste.rs/hottest.json"


def fetch_top_posts_raw(limit: int = 10) -> list:
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(LOBSTERS_HOTTEST_URL, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()
