import csv
from pathlib import Path
from matplotlib import pyplot as plt
from datetime import datetime

scvPath = Path(__file__).resolve().parent / 'weather_data'

path1 = Path(scvPath / 'sitka_weather_2021_simple.csv')
lines = path1.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
#跳过表头
header = next(reader)

#提取最高最低温度，日期
dates,highs,lows = [],[],[]
for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

plt.style.use('default')
fig,ax = plt.subplots()
ax.plot(dates,highs,color='red',alpha = 0.5)
ax.plot(dates,lows,color='blue',alpha = 0.5)
ax.fill_between(dates,highs,lows,facecolor = 'blue',alpha = 0.1)


ax.set_title("Daily High and Low Temperatures, 2021",fontsize = 24)
#x轴标题不添加
ax.set_xlabel('',fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F",fontsize = 16)
ax.minorticks_on()
#ax.tick_params(labelsize =8)


plt.show()


