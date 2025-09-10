import json 
from pathlib import Path

data_path = Path(__file__).resolve().parent / 'eq_data'
file = data_path / 'eq_data_1_day_m1.geojson'

contents =  file.read_text(encoding='utf-8')
all_eq_datas = json.loads(contents)
#print(all_eq_data)

all_eq_dicts = all_eq_datas['features']

# 地震等级列表
mags = []
for eq_dicts  in all_eq_dicts:
    mag =  eq_dicts['properties']['mag']
    mags.append(mag)

print(mags[:10])
