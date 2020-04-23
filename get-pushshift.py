# import pandas as pd
import requests
import json
import csv
import time
import datetime
from datetime import timedelta

firstPostCreatedUtc = 1407254907 # 08/05/2014 @ 4:08pm (UTC)

def appendToFile(fileNamePreFix, data):
    fileName = fileNamePreFix + "_reddit-posts.txt"
    f = open(fileName, "a")
    f.write(data)
    f.close()

def getUrl(before, after):
    subreddit = 'mynoise'
    sort = 'desc'
    sortType = 'created_utc'
    fields = ['id', 'title', 'full_link', 'selftext', 'author', 'created_utc']
    fields = ",".join(map(str,fields))
    pushshiftUrl = 'https://api.pushshift.io/reddit/search/submission/?subreddit={}&sort={}&sort_type={}&after={}&before={}&fields={}'
    return pushshiftUrl.format(subreddit, sort, sortType, after, before, fields)

def getPushshiftData():
    now = int(time.time())
    monthSeconds = 2678400
    lastUtc = now - 3 * monthSeconds # get ~3 months as a test
    # lastUtc = firstPostCreatedUtc
    startUtc = now
    index = 0
    fileCount = 0
    while startUtc >= lastUtc:
        endUtc = startUtc - monthSeconds
        url = getUrl(startUtc, endUtc)
        print(url)
        r = requests.get(url)
        data = json.loads(r.text)

        if len(data['data']) == 0:
            print('no data found')
            continue

        if index % 4 == 0:
            fileCount += 1

        appendToFile(str(fileCount), r.text)
        lastCreatedUtc = data['data'][-1]["created_utc"]

        if lastCreatedUtc == firstPostCreatedUtc:
            break

        print('saved to endUtc: ' + str(endUtc))
        startUtc = endUtc - 1
        index += 1
    
def main():
    getPushshiftData()
    print('fin')

def testMain():
    before = 1587340800
    after = 1584662400
    url = getUrl(after, before)
    print(url)

main()

def testy():
    x = 0
    while x < 20:
        x += 1
        if x % 2 == 0:
            print(x)
