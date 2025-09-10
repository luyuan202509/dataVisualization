from re import sub
import requests
import plotly.express as px

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(url)
#print(f'status :{response.status_code}')
submission_ids_dict = response.json()
submission_dicts = []
for submission_id in submission_ids_dict[:20]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    response = requests.get(url)
    #print(f'id:{submission_id}\tstatus:{response.status_code}')
    response_dict = response.json()
    submission_dict = {
        'title': response_dict['title'],
        'link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants',0)
    }

    submission_dicts.append(submission_dict)

sorted_submission_dicts = sorted(submission_dicts,key = lambda k:k['comments'],reverse = True)

# 处理文章的信息
for submission_dict in sorted_submission_dicts:
    print(f'infomation: {submission_dict}')
    break