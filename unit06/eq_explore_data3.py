import json 
from pathlib import Path

data_path = Path(__file__).resolve().parent / 'eq_data'
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
    
print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])

