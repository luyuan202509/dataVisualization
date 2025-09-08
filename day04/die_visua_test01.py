from die import Die
import pygal
'''同时掷2个骰子'''
from pathlib import Path
# 保存到当前脚本所在目录的 image 子目录（/dataVisualization/day04/image）
image_dir = Path(__file__).resolve().parent / "image"
image_dir.mkdir(parents=True, exist_ok=True)


die6 = Die()
die10 = Die(10)
results = []
for row_num in range(50000):
    s = die6.row() + die10.row()
    results.append(s)

# 分析结果
frequencies = []
max_size = die6.num_size + die10.num_size
for value in range(2,max_size +1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 进行格式化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_lable = list(range(2,17,1))

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10',frequencies)
svg_dir = image_dir / 'die_visual2.svg'
hist.render_to_file(svg_dir)

