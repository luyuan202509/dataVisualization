from plotly.graph_objs.layout import xaxis
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
repo_names, stars,hover_texts = [], [],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(float(repo_dict['stargazers_count']))
    owner = repo_dict['owner']['login']
    description = repo_dict['description']

    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

title = '"Most-Starred Python Projects on GitHub'
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x = repo_names,y = stars,title = title,labels = labels,hover_name= hover_texts)
fig.update_layout(title_x = 0.5,
                  title_font_size = 28, 
                  xaxis_title = 24,
                  yaxis_title = 24,
                  )

fig.show()