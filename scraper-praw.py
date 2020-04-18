import praw
from urllib.parse import urlparse
from urllib.parse import parse_qs

reddit = praw.Reddit('bot1', user_agent='bot1 user agent')

print(reddit.read_only)

for submission in reddit.subreddit('mynoise').hot(limit=10):
    if submission.url.startswith('https://mynoise.net/superGenerator.php?'):
       print(submission.title)
       print(submission.url)
       parsed = urlparse(submission.url)
       qs = parse_qs(parsed.query)
       for key in qs:
          print(key, '->', qs[key])



