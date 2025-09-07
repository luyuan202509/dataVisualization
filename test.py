from pathlib import Path
image_dir = Path.cwd().parent / "image"
image_dir.mkdir(parents=True, exist_ok=True)
print(image_dir)