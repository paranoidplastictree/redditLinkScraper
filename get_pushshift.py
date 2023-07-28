##########################################################################################
# file: get_pushshift.py
# Requests all r/mynoise posts from pushshift.py, starting with most recent
# TODO: Check date or post Id of last scrape performed to prevent unnecessary re-scraping
##########################################################################################

import os
import requests
import json
import time
import datetime
from datetime import timedelta

script_dir = os.path.dirname(__file__)
rel_output_path = '/data/redditPostData'
FIRST_POST_CREATED_UTC = 1407254907 # 08/05/2014 @ 4:08pm (UTC)
MONTH_IN_SECONDS = 2678400
TIME_SPAN = 12 * MONTH_IN_SECONDS

def append_to_file(start_utc, end_utc, data):
    file_name_format = "{}_{}.json"
    file_name = file_name_format.format(start_utc, end_utc)
    path = os.path.join(script_dir, rel_output_path, file_name)
    f = open(path, "a")
    f.write(data)
    f.close()

def get_url(before, after):
    subreddit = 'mynoise'
    size = 1000
    sort = 'desc'
    sort_type = 'created_utc'
    fields = ['id', 'title', 'full_link', 'selftext', 'author', 'created_utc', 'is_self', 'url', 'score']
    fields = ",".join(map(str,fields))
    pushshift_url = 'https://api.pushshift.io/reddit/search/submission/?subreddit={}&sort={}&sort_type={}&after={}&before={}&fields={}&size={}'
    return pushshift_url.format(subreddit, sort, sort_type, after, before, fields, size)

def print_progress(subs_found, end_utc):
    end_date = datetime.datetime.utcfromtimestamp(end_utc)
    formatted_end_date = end_date.strftime("%h %d, %Y %H:%M")
    print(str(subs_found) + " results found for end date: " + formatted_end_date)

def fetch_data(start_utc, end_utc):
    url = get_url(start_utc, end_utc)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)

    subs_found = len(data['data'])
    print_progress(subs_found, end_utc)
    if subs_found == 0:
        return 0

    append_to_file(start_utc, end_utc, r.text)
    print('saved to end_utc: ' + str(end_utc))
    return subs_found

# def get_all_submissions(start_utc):
    # total_subs = 0
    # while start_utc >= FIRST_POST_CREATED_UTC:
    #     end_utc = start_utc - TIME_SPAN
    #     subs_found = fetch_data(start_utc, end_utc)        
    #     total_subs += subs_found
    #     start_utc = end_utc
    # print(str(total_subs) + " total subs found")

def get_all_submissions_in_range(start_utc, range_end_utc):
    total_subs = 0
    while start_utc >= range_end_utc:
        end_utc = start_utc - TIME_SPAN
        subs_found = fetch_data(start_utc, end_utc)        
        total_subs += subs_found
        start_utc = end_utc
    print(str(total_subs) + " total subs found")
    
def main():
    start_seconds = int(time.time())
    # get_all_submissions_in_range(start_seconds, FIRST_POST_CREATED_UTC) #gets all subs since first post
    last_known_post_utc = 1587785797
    get_all_submissions_in_range(start_seconds, last_known_post_utc + 1)

    print('finished processing')

main()