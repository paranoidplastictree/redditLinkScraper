##########################################################################################
# file: parse_post_data.py
# 1. Parses posts and links gathered via get_pushshift.py
# 2. Performs noise machine info lookup for each link found
# 3. Creates supergen meta and saves to file
#
# TODO:
# > regex pattern for links without link text
# > Save supergens to file
# > Check date or post Id of last scrape performed to prevent unnecessary re-scraping
##########################################################################################

import os
import json
import time
import datetime
import re
from datetime import timedelta
import modules.logger as logger
from classes.NoiseMachineService import NoiseMachineService

script_dir = os.path.dirname(__file__)
rel_input_path = '/redditPostData'
supergen_posts = []
nm_svc = NoiseMachineService()

def __get_supergen(post, title, url, noise_machines):
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

def __try_add_supergen(post, title, url):
    noise_machines = nm_svc.get_noise_machines(url)
    supergen = __get_supergen(post, title, url, noise_machines)
    if (supergen):
        supergen_posts.append(supergen)
        return True
    else:
        logger.error("Failed to build supergen")
        return False

def __parse_self_post(submission):
    # TODO: Verify if any self-posts contain links that are NOT prefaced with "[some attempt at a title]""
    # url_pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    # matches all occurrences of: [the-supergen-title](the-supergen_mynoise_url)
    text_url_pattern = r"(?i)(?<=\[)[^\]]+\]\(http[s]?://mynoise.net/supergenerator\.php[^\)]+(?=\))"
    matches = re.findall(text_url_pattern, submission["selftext"])
    isSingleLink = len(matches) == 1

    # some may have more than one valid supergen url
    for match in enumerate(matches):
        matchPair = match.split("](")
        title = matchPair[0]
        url = matchPair[1]
        __try_add_supergen(submission, title, url)

    # todo: create pattern to match links without link text
    non_titled_url_pattern = r""
    matches = re.findall(non_titled_url_pattern, submission["selftext"])
    isSingleLink = len(matches) == 1
    postTitle = submission["title"]
    for idx, match in enumerate(matches):
        linkTitle = postTitle if isSingleLink else "{} {}".format(postTitle, str(idx + 1))
        __try_add_supergen(submission, linkTitle, match)

def __parse_link(submission):
    noise_machines = nm_svc.get_noise_machines(submission["url"])
    if len(noise_machines) < 2:
        return
    supergen = __get_supergen(submission, submission["title"], submission["url"], noise_machines)
    supergen_posts.append(supergen)

def __parse_submissions(data):
    for submission in data["data"]:
        if submission["is_self"]: __parse_self_post(submission)
        else: __parse_link(submission)

def processFiles():
    # path = "c:/dev/redditLinkScraper/redditPostData/"
    path = os.path.join(script_dir, rel_input_path)
    for filename in os.listdir(path):
        if filename.endswith(".json") == False: continue
        f = open(filename)
        data = json.loads(f)
        f.close()
        __parse_submissions(data)

# processFiles()
def processFile():
    f = open("c:/dev/redditLinkScraper/test.json")
    data = json.load(f)
    f.close()
    __parse_submissions(data)
    print("fin")

processFile()