from pathlib import Path
import csv 
import plotly.express  as px
import pandas as pd

parent_path = Path(__file__).resolve().parent



data_path = Path(__file__).resolve().parent / 'eq_data'
file = data_path / 'world_fires_1_day.csv'

lines =  file.read_text(encoding='utf-8').splitlines()
csv_reader = csv.reader(lines)
#表头
head_line = next(csv_reader)

lats, lons, brights = [], [], []
for row in csv_reader:
    try:
        lat = float(row[0])
        lon = float(row[1])
        bright = float(row[2])
    except ValueError:
        # 对于无效行，显示原始的日期信息
        print(f"Invalid data for {row[5]}")
    else:
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

data = pd.DataFrame(
    data= zip(lons, lats, brights),
    columns= ['经度','纬度','火灾强度']
)
#print(data)

fig = px.scatter(
    data,
    x = '经度',
    y = '纬度',
    range_x = [-200,200],
    range_y=[-90,90],
    width= 800,
    height= 800,
    title='全球火灾散点图',
    color= '火灾强度',
    color_continuous_scale='hot',  # 或 'Turbo'、'Plasma'、'' 等
    hover_name = '火灾强度',
    #hover_data='日期'
    
)

html_path = parent_path / 'html'
html_file = html_path / 'world_fire.html'
fig.write_html(html_file)
fig.show()
