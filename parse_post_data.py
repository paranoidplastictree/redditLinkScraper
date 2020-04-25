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

def get_noise_machines(url):
    return ()
    # python parse url, domain, QS
    # https://mynoise.net/superGenerator.php?g1=binauralBrainwaveGenerator.php?c%3D3%26l%3D50464238343027242118&g2=twilightSoundscapeGenerator.php?c%3D3%26l%3D70500000353500000050&g3=windchimesGenerator.php?c%3D3%26l%3D00171423000038516762&g4=cabinNoiseGenerator.php?c%3D3%26l%3D80664570170000000000&g5
    # todo: does it begin with http(s)://mynoise.net/superGenerator.php
    # todo: does it have at least 2 supergens

def parse_self_post(submission):
    self_text = submission["selftext"]
    # todo: parse self_text:
    # --> some may have more than one valid supergen url
    # --> some may not have link text

def parse_link(submission):
    noise_machines = get_noise_machines(submission["url"])
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