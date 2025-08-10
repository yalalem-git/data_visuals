import requests
import json
from operator import itemgetter

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
print(f"Status Code: {response.status_code}")


submission_ids = response.json()
submission_dicts = []


for submission_id in submission_ids[:45]:
      custom_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
      custom_response = requests.get(custom_url)


      print(f"id: {submission_id}\tStatus: {custom_response.status_code}")
      response_dict = custom_response.json()
      
      try:
          submission_dict = {
                "title" : response_dict['title'],
                'url' : response_dict['url'],
                'hn_link' : f"https://news.ycombinator.com/item?id={submission_id}",
                "comments" : response_dict["descendants"]
            }
      except KeyError as e:
          print("Key Error")
      else:
          submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key = itemgetter('comments', reverse = True))



for submission_dict in submission_dicts:
    print(f"\nTitle : {submission_dict["title"]}")
    print(f"\nDiscussion Link : {submission_dict["hn_link"]}")
    print(f"Article Link : {submission_dict['url']}")
