import csv
from pathlib import Path
from matplotlib import pyplot as plt
from datetime import datetime

scvPath = Path(__file__).resolve().parent / 'weather_data'

path1 = Path(scvPath / 'sitka_weather_07-2021_simple.csv')
lines = path1.read_text().splitlines()


reader = csv.reader(lines)
header_row  = next(reader)

#提取最高温度
dates,highs = [],[]
'''
for index,column_header in enumerate(header_row):
    print(index,column_header)
'''
for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%M-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

plt.style.use('default')
fig,ax = plt.subplots()
ax.plot(dates,highs,color='red')

ax.set_title("Daily High Temperatures, July 2021",fontsize = 14)
ax.set_xlabel('Time',fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F",fontsize = 16)
ax.minorticks_on()
ax.tick_params(labelsize =8)


plt.show()


