from shutil import which
import matplotlib.pyplot as plt
'''绘制散点图'''
plt.scatter(2,4,s = 200)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14) 

# 设置刻度大小
plt.tick_params(axios = 'both',which= 'major',lablesize = 14)

plt.plot()

plt.show()
