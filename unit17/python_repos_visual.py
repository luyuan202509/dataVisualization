import requests as req
import plotly.express as px

#url = 'https://api.github.com/search/repositories?q=language:python+sort:stars'
url = 'http://localhost:19990/region/gihub/repos'
headers = {"Accept": "application/vnd.github.v3+json"}
responses = req.get(url,headers)

# 处理结果
response_dict =  responses.json()
repo_dicts = response_dict['items']
print(f"Complete results: {not response_dict['incomplete_results']}")

# 处理仓库相关信息
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(float(repo_dict['stargazers_count']))

fig = px.bar(x = names,y = stars)
fig.show()