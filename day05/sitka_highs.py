import csv
from pathlib import Path 

scvPath = Path(__file__).resolve().parent / 'weather_data'

path1 = Path(scvPath / 'sitka_weather_07-2021_simple.csv')
lines = path1.read_text().splitlines()

reader = csv.reader(lines)
header_row  = next(reader)

for index,column_header in enumerate(header_row):
    print(index,column_header)

