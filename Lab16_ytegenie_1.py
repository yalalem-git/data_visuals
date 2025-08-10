"""
Returning Most Popular Articles from Hacker News website
by: Yalalem Tegenie
The code is devloped to retrive the top 45 articles by popularity from 'Hacker News' website by editing the lecture video
10 August 2025

"""

import requests
from operator import itemgetter

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
print(f"Status Code: {response.status_code}")

submission_ids = response.json()
submission_dicts = []

for submission_id in submission_ids[:45]:
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    item_response = requests.get(item_url)
    #print(f"id: {submission_id}    Status: {item_response.status_code}")

    item_data = item_response.json()

    if not item_data:
        continue  # skip if None

    try:
        comments = item_data['descendants']
    except KeyError:
        comments = 0  # default if key is missing

    submission_dict = {
        "title": item_data.get("title", "No title"),
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "url": item_data.get("url", ""),
        "comments": comments
    }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for i, submission in enumerate(submission_dicts, start=1):
    print(f"{i}. Title: {submission['title']}")
    print(f"   Discussion Link: {submission['hn_link']}")
    print(f"   Article Link: {submission['url']}\n")