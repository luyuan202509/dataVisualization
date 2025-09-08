from die import Die
import pygal
'''同时掷2个骰子'''
from pathlib import Path
# 保存到当前脚本所在目录的 image 子目录（/dataVisualization/day04/image）
image_dir = Path(__file__).resolve().parent / "image"
image_dir.mkdir(parents=True, exist_ok=True)


die = Die()
results = []
for row_num in range(1000):
    s = die.row()
    results.append(s)

# 分析结果
frequencies = []
for value in range(1,die.num_size +1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 进行格式化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_lable = [1,2,3,4,5,6]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6',frequencies)
svg_dir = image_dir / 'die_visual.svg'
hist.render_to_file(svg_dir)

