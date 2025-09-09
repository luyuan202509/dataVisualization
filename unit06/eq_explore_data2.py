import json 
from pathlib import Path

data_path = Path(__file__).resolve().parent / 'eq_data'
file = data_path / 'eq_data_1_day_m1.geojson'

contents =  file.read_text(encoding='utf-8')
all_eq_datas = json.loads(contents)
#print(all_eq_data)

new_file = data_path / 'readable_eq_data_new2.geojson'

#readble_contents =  json.dumps(all_eq_datas,indent=4)
#new_file.write_text(readble_contents)

with open(new_file,'w',encoding="utf-8") as f:
    json.dump(all_eq_datas,f,indent=4,ensure_ascii=False)
