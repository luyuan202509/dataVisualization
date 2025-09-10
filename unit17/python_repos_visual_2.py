from plotly.graph_objs.layout import xaxis
import requests as req
import plotly.express as px
''' 添加可单击的链接 '''

#url = 'https://api.github.com/search/repositories?q=language:python+sort:stars'
url = 'http://localhost:19990/region/gihub/repos'
headers = {"Accept": "application/vnd.github.v3+json"}
responses = req.get(url,headers)

# 处理结果
response_dict =  responses.json()
repo_dicts = response_dict['items']
print(f"Complete results: {not response_dict['incomplete_results']}")

# 处理仓库相关信息
repo_links, stars,hover_texts = [], [],[]
for repo_dict in repo_dicts:
    repo_name  = repo_dict['name'],
    repo_url = repo_dict['html_url'],
    repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>")
    owner = repo_dict['owner']['login'],
    stars.append(float(repo_dict['stargazers_count']))
    description = repo_dict['description']

    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

title = '"Most-Starred Python Projects on GitHub'
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x = repo_links,y = stars,title = title,labels = labels,hover_name= hover_texts)
fig.update_layout(title_x = 0.5,
                  title_font_size = 28, 
                  xaxis_title = 24,
                  yaxis_title = 24,
                  )
fig.update_traces(marker_color = 'rgb(60,100,150)',marker_opacity = 0.6)

fig.show()