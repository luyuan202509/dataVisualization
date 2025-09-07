import matplotlib.pyplot as plt 
from random_walk import RandomWalk
'''隐藏坐标轴'''

while True:
    rw = RandomWalk()
    rw.fill_walk()
    #轨迹列表
    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values,rw.y_values,s=15,c = point_numbers,cmap = plt.cm.Blues,edgecolors= 'none')
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100) 
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c = 'red',edgecolors= 'none',s = 100)
    
    #隐藏坐标轴
    ax = plt.gca()
    ax.set_axis_off()
    # 或者,这里会有问题
    #ax.xaxis.set_visible(False)
    #ax.yaxis.set_visible(False)

    plt.show()

    keep_running = input('make another walk?(y/n): ')
    if keep_running == 'n':
        break
