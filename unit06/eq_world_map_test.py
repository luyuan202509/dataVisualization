import json 
from pathlib import Path
import plotly.express  as px
import pandas as pd

'''
测试3， 最近发生的地震 2025，8月份地震散点图
'''

parent_path =  Path(__file__).resolve().parent

data_path = parent_path / 'eq_data'
file = data_path / 'all_month.geojson'

# 将数据作为字符串读取并转换为 Python 对象
contents =  file.read_text(encoding='utf-8')
all_eq_datas = json.loads(contents)

all_eq_dicts = all_eq_datas['features']
#print(all_eq_dicts)



mags,lons,lats,titles = [],[],[],[]
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties'].get('mag'))
    titles.append(eq_dict['properties']['title'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])

data = pd.DataFrame(
    data = zip(lons,lats,titles,mags),
    columns= ['经度','纬度','位置','震级']
)
# 震级是空或小于 0的震级设置为0
data['震级'] = pd.to_numeric(data['震级'], errors='coerce').fillna(0).clip(lower=0)

# 检查 地震震级出现负数,scatter(参数不能是负数)
'''
for _, _, title, mag in data.itertuples(index=False, name=None):
    if mag < 0:
        print(title, mag)
'''



fig =  px.scatter(
    data,
    x = '经度',
    y = '纬度',
    range_x=[-200,200],
    range_y=[-180,180],
    width=800,
    height=800,
    title= '2025年8月全球地震散点图',
    size= '震级',
    size_max= 10,
    color='震级',
    color_continuous_scale= 'rainbow',
    hover_data='位置'
)


html_path = parent_path / 'html'
html_file = html_path / 'all_month2020508.html'

fig.write_html(html_file)
fig.show()

