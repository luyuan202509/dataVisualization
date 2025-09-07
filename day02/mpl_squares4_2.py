import matplotlib.pyplot as plt
'''绘制一系列散点图'''
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25] 
#plt.scatter(x_values,y_values,s = 500)
plt.scatter(x_values,y_values,s = 1000,edgecolors='red')


# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14) 
plt.plot()

plt.show()
