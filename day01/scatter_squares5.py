''' 自动保存图表 savefig '''
import matplotlib.pyplot as plt
from pathlib import Path


# 保存到当前脚本所在目录的 image 子目录（/dataVisualization/image）
image_dir = Path(__file__).resolve().parent / "image"
image_dir.mkdir(parents=True, exist_ok=True)

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,edgecolors='none',cmap=plt.cm.Greens)
plt.axis([0,1100,0,1100000])

out_path = image_dir / 'squares_plot.png'
plt.savefig(out_path, dpi=300, bbox_inches='tight')
print(f"图像已保存到: {out_path}")
plt.show(block=False)


