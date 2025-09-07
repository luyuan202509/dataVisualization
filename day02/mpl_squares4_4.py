import matplotlib.pyplot as plt
'''绘制一系列散点图'''
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values] 
#plt.scatter(x_values,y_values,s = 100,c='red',edgecolors= 'none')
#plt.scatter(x_values,y_values,s = 100,c='red',edgecolors='green')
#plt.scatter(x_values,y_values,s = 100,c='red',edgecolors= 'none')
plt.scatter(x_values,y_values,s=100,c =y_values,edgecolors='none',cmap = plt.cm.Blues)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14) 

# 
plt.plot()

plt.show()
