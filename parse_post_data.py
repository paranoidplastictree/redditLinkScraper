import os
import json
import time
import datetime
from datetime import timedelta

supergen_posts = ()

def get_supergen(post, title, url, noise_machines):
    if len(noise_machines) < 2:
        print("Not enough noise machines")
        return

    return {
        "post_id": post["id"],
        "author": post["author"],
        "created_utc": post["created_utc"],
        "reddit_url": post["full_link"],
        "url": url,
        "title": title,
        "noise_machines": noise_machines
    }


def parse_self_post(submission):
    # TODO: Verify if any self-posts contain links that are NOT prefaced with "[some attempt at a title]""
    url_pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    text_url_pattern = r"(?i)(?<=\[)[^\]]+\]\(http[s]?://mynoise.net/supergenerator\.php[^\)]+(?=\))"
    post_title = submission["title"]
    reddit_link = submission["full_link"]
    created_utc = submission["created_utc"]
    matches = re.findall(text_url_pattern, submission["selftext"])
    matchCount = len(matches)
    for idx, match in enumerate(matches):
        matchPair = match.split("](")
        title = matchPair[0] if matchCount == 1 else "{} {}".format(matchPair[0], str(idx + 1))
        url = matchPair[1]
        noise_machines = get_noise_machines(url)
        # todo: parse self_text:
        # [x] some may have more than one valid supergen url
        # [ ] some may not have link text

def parse_link(submission):
    noise_machines = get_noise_machines(submission["url"])
    if len(noise_machines) < 2:
        return
    supergen = get_supergen(submission, submission["title"], submission["url"], noise_machines])
    supergen_posts.append(supergen)

def parse_submissions(data):
    for submission in data["data"]:
        if submission["is_self"]: parse_self_post(submission)
        else: parse_link(submission)

def processFiles():
    directory = "c:/dev/redditLinkScraper/redditPostData/"
    for filename in os.listdir(directory):
        if filename.endswith(".json") == False: continue
        f = open(filename)
        data = json.loads(f)
        parse_submissions(data)

# processFiles()
def processFile():
    f = open("c:/dev/redditLinkScraper/test.json")
    data = json.load(f)
    parse_submissions(data)
    print("fin")

processFile()