import requests as req
import plotly.express as px

#url = 'https://api.github.com/search/repositories?q=language:python+sort:stars'
url = 'http://localhost:19990/region/gihub/repos'
headers = {"Accept": "application/vnd.github.v3+json"}
responses = req.get(url,headers)
response_dict =  responses.json()
#print(response_dict.keys())

repo_dicts = response_dict['items']
#print(f'Repositories returned: {len(repo_dicts)}')

# 第一个仓库
print("\n========Selected information about first repository: ===========")
repo_dict = repo_dicts[0]

print(f"仓库名称：{repo_dict['name']}")
print(f"仓库作者: {repo_dict['owner']['login']}")
print(f"仓库星星获得数量：{repo_dict['stargazers_count']}")
print(f"仓库的url: {repo_dict['html_url']}")
print(f"仓库的描述：{repo_dict['description']}")

