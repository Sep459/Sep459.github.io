import os
from PIL import Image

# === 配置 ===
'''
img_dir = r"F:\Hexo\source\images\gallery"
img_dir = r"F:\Hexo\source\images\daily"
img_dir = r"F:\Hexo\source\images\pet"
img_dir = r"F:\Hexo\source\images\food"
'''
img_dir = r"F:\Hexo\source\images\pet"

max_side = 2000   # 最大边长
quality = 85      # 压缩质量
exts = ('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff')

# === 压缩函数 ===
def compress_and_resize(filepath):
    try:
        old_size = os.path.getsize(filepath)
        img = Image.open(filepath)
        img_format = img.format or 'JPEG'

        # 判断是否需要缩放
        w, h = img.size
        if max(w, h) > max_side:
            scale = max_side / max(w, h)
            img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

        # 统一保存逻辑
        img.save(filepath, format=img_format, quality=quality, optimize=True)

        new_size = os.path.getsize(filepath)
        if new_size < old_size:
            print(f"{os.path.basename(filepath)}: {old_size/1024/1024:.2f}MB → {new_size/1024/1024:.2f}MB")
        else:
            print(f"{os.path.basename(filepath)} 不压缩")

    except Exception as e:
        print(f"❌ 处理失败 {filepath}: {e}")


# === 遍历目录 ===
for filename in os.listdir(img_dir):
    if not filename.lower().endswith(exts):
        continue
    compress_and_resize(os.path.join(img_dir, filename))

print("🎯 全部完成。")
