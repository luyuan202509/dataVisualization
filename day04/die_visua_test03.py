from die import Die
import pygal
'''同时掷3个骰子'''
from pathlib import Path
# 保存到当前脚本所在目录的 image 子目录（/dataVisualization/day04/image）
image_dir = Path(__file__).resolve().parent / "image"
image_dir.mkdir(parents=True, exist_ok=True)


die1 = Die()
die2 = Die()
die3 = Die()
results = []
for row_num in range(int(50000)):
    s = die1.row() + die2.row() + die3.row()
    results.append(s)

# 分析结果
frequencies = []
max_size = die1.num_size * 3
for value in range(2,max_size +1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 进行格式化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 and D10 dice 500000 times"
hist.x_lable = list(range(3,18,1))

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('3 d6',frequencies)
svg_dir = image_dir / 'die_visual5.svg'
hist.render_to_file(svg_dir)

