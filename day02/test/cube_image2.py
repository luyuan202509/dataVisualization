import matplotlib.pyplot as plt 
from pathlib import Path


curDir =  Path(__file__).resolve().parent

x_values = list(range(1,50001,1))
y_values = [n**3 for n in x_values ]

# 画点集
plt.scatter(x_values,y_values,s = 100,c = y_values,edgecolors='none',cmap=plt.cm.Blues)

# 显示次刻度线
plt.minorticks_on()

plt.tick_params(axis= 'both',which = 'major',
                direction = 'out',length = 8,width =2,color = 'red')
plt.tick_params(axis= 'both',which = 'minor',
                direction = 'out',length = 4,width = 1,color = 'blue')

# 开画
plt.plot()
plt.show()