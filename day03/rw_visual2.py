import matplotlib.pyplot as plt 
from random_walk import RandomWalk
'''增加点运动轨迹'''

while True:
    rw = RandomWalk()
    rw.fill_walk()
    #轨迹列表
    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values,rw.y_values,s=15,c = point_numbers,cmap = plt.cm.Blues,edgecolors= 'none')
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100) 
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c = 'red',edgecolors= 'none',s = 100)
    plt.show()

    keep_running = input('make another walk?(y/n): ')
    if keep_running == 'n':
        break
