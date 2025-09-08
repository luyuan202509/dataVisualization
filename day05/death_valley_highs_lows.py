from importlib import readers
from matplotlib import pyplot as plt 
import csv 
from  pathlib import Path
from datetime import datetime 

parent_path = Path(__file__).resolve().parent / 'weather_data'
file = parent_path / 'death_valley_2021_simple.csv'
line = file.read_text().splitlines()

readers = csv.reader(line)
# 跳过头行
header_row = next(readers)
'''
for index ,column_header in enumerate(header_row):
    print(index,column_header) 
'''

# 提取日期，最高温，最低温，
dates, highs, lows = [], [], []
for row in readers:
    date= datetime.strptime(row[2],'%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {date}") 
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

plt.style.use('default')
fig,ax = plt.subplots()
ax.plot(dates,highs,color = 'red',alpha=0.5)
ax.plot(dates,lows,color = 'blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor = 'blue',alpha = 0.1)

title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title,fontsize= 20)
ax.set_xlabel('',fontsize =16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F',fontsize = 16)

plt.show()
