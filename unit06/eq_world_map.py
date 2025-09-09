import json 
from pathlib import Path
import plotly.express  as px
import pandas as pd

parent_path =  Path(__file__).resolve().parent

data_path = parent_path / 'eq_data'
file = data_path / 'eq_data_1_day_m1.geojson'

# 将数据作为字符串读取并转换为 Python 对象
contents =  file.read_text(encoding='utf-8')
all_eq_datas = json.loads(contents)
#print(all_eq_data)

# 查看地震中所有地震
all_eq_dicts = all_eq_datas['features']
#print(all_eq_dicts)

mags,titles,lons,lats, = [],[],[],[] 
for eq_dict in all_eq_dicts:
    mag   = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon   = eq_dict['geometry']['coordinates'][0]
    lat   = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data  = pd.DataFrame(
    data = zip(lons,lats,titles,mags),
    columns= ['经度','纬度','位置','震级']
)

fig = px.scatter(
           data,
           x='经度',
           y='纬度',
           range_x = [-200,200],
           range_y=[-90,90],
           width= 800,
           height= 800,
           title= '全球地震散点图',
           size= '震级',
           size_max=10
)

html_path = parent_path / 'html'
html_file = html_path / 'global_earthquakes.html'
fig.write_html(html_file)
fig.show()
