import csv
from pathlib import Path
from matplotlib import pyplot as plt

scvPath = Path(__file__).resolve().parent / 'weather_data'

path1 = Path(scvPath / 'sitka_weather_07-2021_simple.csv')
lines = path1.read_text().splitlines()


reader = csv.reader(lines)
header_row  = next(reader)

#提取最高温度
highs = []
'''
for index,column_header in enumerate(header_row):
    print(index,column_header)
'''
for row in reader:
    high = int(row[4])
    highs.append(high)

plt.style.use('default')
fig,ax = plt.subplots()
ax.plot(highs,color='red')

ax.set_title("Daily High Temperatures, July 2021",fontsize = 14)
ax.set_xlabel('Time',fontsize = 16)
ax.set_ylabel("Temperature (F",fontsize = 16)
ax.minorticks_on()
ax.tick_params(labelsize =8)


plt.show()


