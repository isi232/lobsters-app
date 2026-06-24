from pipeline.db import init_db
from pipeline.fetcher import fetch_top_posts_raw
from pipeline.transformer import transform_posts
from pipeline.loader import load_posts


def run():
    print("=== Lobsters Top Posts Pipeline ===\n")

    print("Step 0: Ensuring database tables exist...")
    init_db()
    print("  ✅ Database ready.\n")

    print("Step 1: Fetching raw data from lobste.rs (hottest)...")
    raw_json = fetch_top_posts_raw(limit=10)
    print(f"  ✅ Fetched {len(raw_json)} raw stories.\n")

    print("Step 2: Transforming raw data into our schema...")
    clean_posts = transform_posts(raw_json, limit=10)
    print(f"  ✅ Transformed {len(clean_posts)} posts.\n")

    print("Step 3: Loading posts into the database...")
    summary = load_posts(clean_posts)
    print(f"  ✅ Inserted: {summary['inserted']}, Updated: {summary['updated']}, "
          f"Total processed: {summary['total']}\n")

    print("=== Pipeline run complete! ===")


if __name__ == "__main__":
    run()
