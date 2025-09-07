import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,edgecolors='none',cmap=plt.cm.Greens)
plt.axis([0,1100,0,1100000])
plt.show()


plt.pause(1)
plt.close()
