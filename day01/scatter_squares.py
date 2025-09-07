import matplotlib.pyplot as plt
plt.scatter(2, 5, s=200) 
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()