##########################################################################################
# file: parse_post_data.py
# 1. Parses reddit posts and links gathered via get_pushshift.py
# 2. Performs noise machine info lookup for each link found (posts have 0 or more links)
# 3. Creates supergen meta and saves to file
#
# TODO:
# > regex pattern for links without link text
# > Save supergens to file
# > Load paths and file names from a config module
##########################################################################################
import os
import modules.fileIO as io
import modules.linkParser as linkParser
from classes.SupergenService import SupergenService

script_dir = os.path.dirname(__file__)
rel_input_path = '/data/redditPostData'
rel_output_path = './data/output'
post_input_path = os.path.join(script_dir, rel_input_path)
output_path = os.path.join(script_dir, rel_output_path)
sg_svc = SupergenService(output_path)

def __add_titled_match(match, submission):
    matchIndex = match[0]
    title_url = match[1].replace("] (", "](")
    title_url = title_url[1:-1] # remove first "[" and last ")" characters
    match_pair = title_url.split("](")
    title = match_pair[0] if matchIndex == 0 else match_pair[0] + " " + str(matchIndex)
    url = match_pair[1]
    sg_svc.add(submission, title, url)

def __parse_titled_matches(submission):
    # TODO: Verify if any self-posts contain links that are NOT prefaced with "[some attempt at a title]""
    # some posts may have more than one valid supergen url, add each of them
    titled_matches = linkParser.find_all_titled_links(submission["selftext"])
    for titled_match in enumerate(titled_matches):
        __add_titled_match(titled_match, submission)

def __add_untitled_url(url, submission, index, match_count):
    is_single = len(match_count) == 1
    post_title = submission["title"]
    link_title = post_title if is_single else "{} {}".format(post_title, str(index + 1))
    sg_svc.add(submission, link_title, url)

def __parse_untitled_matches(submission):
    # TODO: create pattern to match links without link text
    untitled_urls = linkParser.find_all_untitled_links(submission["selftext"])
    match_count = len(untitled_urls)
    for idx, untitled_url in enumerate(untitled_urls):
        __add_untitled_url(untitled_url, submission, idx, match_count)

def __parse_self_post(submission):
    __parse_titled_matches(submission)
    #__parse_untitled_matches(submission)

def __parse_link(submission):
    sg_svc.add(submission, submission["title"], submission["url"])

def __parse_submissions(data):
    for submission in data["data"]:
        if submission["is_self"]: __parse_self_post(submission)
        else: __parse_link(submission)

def __process_files():
    # path = "c:/dev/redditLinkScraper/data/redditPostData/"
    file_names = io.list_dir(post_input_path)
    for filename in file_names:
        data = io.read_json(filename)
        if (data): __parse_submissions(data)

def __process_file():
    data = io.read_json("c:/dev/redditLinkScraper/test.json")
    if (data): __parse_submissions(data)

def main():
    __process_file()
    sg_svc.save_all()
    print("fin")

main()
