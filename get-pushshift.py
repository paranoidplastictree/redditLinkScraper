# import pandas as pd
import requests
import json
import csv
import time
import datetime
from datetime import timedelta

firstPostCreatedUtc = 1407254907 # 08/05/2014 @ 4:08pm (UTC)
monthSeconds = 2678400
timeSpanPerRequest = 12 * monthSeconds

def appendToFile(startUtc, endUtc, data):
    fileNameFormat = "{}_{}.json"
    fileName = fileNameFormat.format(startUtc, endUtc)
    f = open(fileName, "a")
    f.write(data)
    f.close()

def getUrl(before, after):
    subreddit = 'mynoise'
    size = 1000
    sort = 'desc'
    sortType = 'created_utc'
    fields = ['id', 'title', 'full_link', 'selftext', 'author', 'created_utc', 'is_self']
    fields = ",".join(map(str,fields))
    pushshiftUrl = 'https://api.pushshift.io/reddit/search/submission/?subreddit={}&sort={}&sort_type={}&after={}&before={}&fields={}&size={}'
    return pushshiftUrl.format(subreddit, sort, sortType, after, before, fields, size)

def getPushshiftData(start):
    totalSubs = 0
    # lastUtc = now - 6 * monthSeconds # get ~6 months as a test
    lastUtc = firstPostCreatedUtc
    startUtc = start

    while startUtc >= lastUtc:
        subsFound = 0
        endUtc = startUtc - timeSpanPerRequest
        url = getUrl(startUtc, endUtc)
        print(url)
        r = requests.get(url)
        data = json.loads(r.text)

        subsFound = len(data['data'])
        totalSubs += subsFound
        endDate = datetime.datetime.utcfromtimestamp(endUtc)
        formattedEndDate = endDate.strftime("%h %d, %Y %H:%M")
        print(str(subsFound) + " results found, last post dated: " + formattedEndDate)

        if subsFound == 0:
            print('no data found')
            continue

        appendToFile(startUtc, endUtc, r.text)

        lastCreatedUtc = data['data'][-1]["created_utc"]
        if lastCreatedUtc == firstPostCreatedUtc:
            break

        print('saved to endUtc: ' + str(endUtc))
        startUtc = endUtc
    
    print(str(totalSubs) + " total subs found")
    
def main():
    startSeconds = int(time.time())
    # startSeconds = 1426993907 # periodically, script fails. It may be a restriction on requests/minute
    getPushshiftData(startSeconds)
    print('fin')

def testMain():
    before = 1587340800
    after = 1584662400
    url = getUrl(after, before)
    print(url)

main()