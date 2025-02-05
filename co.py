import praw

# Reddit API Credentials (Replace with your own)
REDDIT_CLIENT_ID = "CB53gf3Pz-Q8JvQ6YWBoQQ"
REDDIT_CLIENT_SECRET = "xakCmPBnUKkL-XzX2kjDD7dlqWCdPg"
USER_AGENT = "script:trump_scrap_app:v1.0 (by u/EggplantMaleficent61)"


# Initialize Reddit API
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=USER_AGENT
)


# Function to scrape a subreddit
def scrape_reddit(subreddit, limit=5):
    subreddit = reddit.subreddit(subreddit)
    print(f"Fetching {limit} posts from r/{subreddit.display_name}...\n")

    for post in subreddit.hot(limit=limit):
        print(f"Title: {post.title}")
        print(f"Author: u/{post.author}")
        print(f"Upvotes: {post.score}")
        print(f"Comments: {post.num_comments}")
        print(f"URL: {post.url}")
        print("-" * 50)

# Example usage
scrape_reddit("trumptweets2", limit=5)




