''' https://hacker-news.firebaseio.com/v0/item/31353677.json '''
import requests
import json 

response = requests.get('https://hacker-news.firebaseio.com/v0/item/31353677.json')
#print(f'status :{response.status_code}')

# 探索数据结构
response_dict = response.json()
print(json.dumps(response_dict,indent=4))
