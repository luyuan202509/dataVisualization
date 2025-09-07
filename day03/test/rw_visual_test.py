'''
修改 rw_visual.py，将其中的 plt.scatter()替换为 plt.plot()。为
模拟花粉在水滴表面的运动路径，向 plt.plot()传递 rw.x_values 和 rw.y_values，并
指定实参值 linewidth。使用 5000 个点而不是 50 000 个点
''' 
import matplotlib.pyplot as plt 
from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()
#plt.scatter(rw.x_values,rw.y_values,s =15)

plt.plot(rw.x_values,rw.y_values,linewidth = 5)

plt.show()