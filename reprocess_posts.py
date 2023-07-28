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
rel_input_path = './data/redditPostData'
rel_output_path = './data/output'
post_input_path = os.path.join(script_dir, rel_input_path)
output_path = os.path.join(script_dir, rel_output_path)
noise_machine_base_path = "https://mynoise.net/NoiseMachines/"
sg_svc = SupergenService(output_path)

# def __add_titled_match(match, submission):
#     matchIndex = match[0]
#     title_url = match[1].replace("] (", "](")
#     title_url = title_url[1:-1] # remove first "[" and last ")" characters
#     match_pair = title_url.split("](")
#     title = match_pair[0] if matchIndex == 0 else match_pair[0] + " " + str(matchIndex)
#     url = match_pair[1]
#     sg_svc.add(submission, title, url)

# def __parse_titled_matches(submission):
#     # some posts may have more than one valid supergen url, add each of them
#     titled_matches = linkParser.find_all_titled_links(submission["selftext"])
#     for titled_match in enumerate(titled_matches):
#         __add_titled_match(titled_match, submission)

# def __add_untitled_url(url, submission, index, match_count):
#     is_single = match_count == 1
#     post_title = submission["title"]
#     link_title = post_title if is_single else "{} {}".format(post_title, str(index + 1))
#     sg_svc.add(submission, link_title, url)

# def __parse_untitled_matches(submission):
#     untitled_urls = linkParser.find_all_untitled_links(submission["selftext"])
#     match_count = len(untitled_urls)
#     for idx, untitled_url in enumerate(untitled_urls):
#         __add_untitled_url(untitled_url, submission, idx, match_count)

# def __parse_self_post(submission):
#     __parse_titled_matches(submission)
#     __parse_untitled_matches(submission)

# def __parse_link(submission):
#     sg_svc.add(submission, submission["title"], submission["url"])

def __map_to_generator_info(nm_endpoint):
    return {
        "id": 0,
        "name": "",
        "href": "./NoiseMachines/" + nm_endpoint,
        "generatorType": "",
        "categories": []
    }

def __process_posts(post_data):
    noise_machine_endpoints = set(list(nm for pd in post_data for nm in pd["undefined_noise_machines"]))
    # generate data in shape of noiseGeneratorInfo.json?
    noise_machines = list(map(__map_to_generator_info, list(noise_machine_endpoints)))
    dict = {
        "listNames": [],
        "noiseMachineCategories": [],
        "noiseMachines": noise_machines
    }
    io.write_dict(dict, output_path, "noiseGeneratorInfo_undefined.json")

def __process_file(file_name):
    path = os.path.join(output_path, file_name)
    data = io.read_json_lines(path)
    if (data): __process_posts(data)

def main():
    __process_file("posts_with_undefined_noise_machines.jsonl")
    sg_svc.save_all()
    print("fin")

main()
