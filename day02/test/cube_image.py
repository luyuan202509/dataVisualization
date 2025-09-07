import matplotlib.pyplot as plt 
from pathlib import Path


curDir =  Path(__file__).resolve().parent

x_values = list(range(1,6,1))
y_values = [n**3 for n in x_values ]

# 画点集
plt.scatter(x_values,y_values,s = 100)


plt.plot()
plt.show();