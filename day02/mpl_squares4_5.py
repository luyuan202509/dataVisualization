import matplotlib.pyplot as plt
from pathlib import Path
# 保存到当前脚本所在目录的 image 子目录（/dataVisualization/image）
image_dir = Path(__file__).resolve().parent / "image"
image_dir.mkdir(parents=True, exist_ok=True)


'''保存图片'''
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values] 
#plt.scatter(x_values,y_values,s = 100,c='red',edgecolors= 'none')
#plt.scatter(x_values,y_values,s = 100,c='red',edgecolors='green')
#plt.scatter(x_values,y_values,s = 100,c='red',edgecolors= 'none')
plt.scatter(x_values,y_values,s=100,c =y_values,edgecolors='none',cmap = plt.cm.Blues)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14) 


print(f'图片目录：{image_dir}')

image_path = image_dir / 'squares_plot2.png'
plt.savefig(image_path)

# 
plt.plot()
plt.show()
