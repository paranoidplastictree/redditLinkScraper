import praw

reddit = praw.Reddit('bot1', user_agent='bot1 user agent')

print(reddit.read_only)

for submission in reddit.subreddit('mynoise').hot(limit=10):
    print(submission.title)