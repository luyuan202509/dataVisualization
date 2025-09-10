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
titles,comments,hover_texts = [],[],[]
for submission_dict in sorted_submission_dicts:
    title = submission_dict['title']
    titles.append(title)
    comments.append(submission_dict['comments'])
    link = submission_dict['link']
    hover_texts.append(f'{title}<br><a href="{link}">{link}</a>')

title = 'Most Popular arcticles on hacker-news'
labels = {'x': 'Articles', 'y': 'comments'}
fig = px.bar(x=titles,
             y=comments,
             title= title,
             labels=labels,
             hover_name=hover_texts)

fig.update_layout(xaxis_title='Articles',
                  yaxis_title='comments',
                  xaxis_tickangle=45,
                  xaxis_tickfont_size=8)
fig.update_traces(marker_color = 'rgb(60,100,150)',marker_opacity = 0.6)

fig.show()