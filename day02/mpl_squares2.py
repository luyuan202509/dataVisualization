import matplotlib.pyplot as plt
'''修改标签文字和线条粗细'''
squares = [1, 4, 9, 16, 25] 
#squares = [n for n in range(1,6,1)]
'''改变线条粗细'''
plt.plot(squares,linewidth = 10)

#设置图表标题，并给坐标轴加上标签
plt.title('Square Numbers',fontsize = 14)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Square of Value',fontsize = 14)

# 启用次刻度
plt.minorticks_on()

# 设置主刻度
plt.tick_params(axis='both', which='major', 
                direction='out', length=8, width=2, color='blue')

# 设置次刻度
plt.tick_params(axis='both', which='minor', 
                direction='in', length=4, width=1, color='red')

plt.show()


