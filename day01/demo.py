import matplotlib.pyplot as plt
squares = [1,4,9,16,25]
plt.plot(squares,linewidth=3,linestyle='--',color='red')

plt.title("Square Numbers",fontsize=24,loc="center")
plt.xlabel("Value",fontsize=14)
plt.ylabel("square of Value",fontsize=14)
plt.tick_params(axis='x',labelsize=18)
print(range(len(squares)))

plt.show()