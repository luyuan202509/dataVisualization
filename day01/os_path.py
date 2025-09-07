from pathlib import Path 

curPath = Path.cwd()
print(f'当前路径：{curPath}')

workPath = Path(__file__).parent  # 脚本所在目录
print(f'工作路径：{workPath}')

# 获取脚本目录下的 image 文件夹
script_dir = Path(__file__).resolve().parent
image_dir = script_dir / 'image'
#image_dir.mkdir(exist_ok=True)
print(f'图片路径: {image_dir}')


