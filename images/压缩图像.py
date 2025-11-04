import os
from PIL import Image

# === 1. 配置 ===
img_dir = r"F:\Hexo\source\images\gallery"
max_size_mb = 4         # 超过这个大小（MB）就压缩
quality = 85            # JPG 压缩质量（建议 80~90）
resize_factor = 0.9     # PNG 时降低尺寸的比例（避免质量太差）

# === 2. 检查并压缩 ===
def compress_image(filepath):
    """压缩单张图片"""
    try:
        img = Image.open(filepath)
        img_format = img.format

        # 暂时存储压缩后的路径（先写到临时文件）
        temp_path = filepath + ".tmp"

        if img_format in ['JPEG', 'JPG']:
            # 重新保存为高质量但体积较小的 JPEG
            img.save(temp_path, format='JPEG', optimize=True, quality=quality)
        elif img_format == 'PNG':
            # PNG 无损压缩+可选缩小尺寸
            w, h = img.size
            img = img.resize((int(w * resize_factor), int(h * resize_factor)))
            img.save(temp_path, format='PNG', optimize=True)
        else:
            print(f"⚠️ 跳过不支持的格式: {filepath}")
            return False

        # 检查压缩效果
        old_size = os.path.getsize(filepath)
        new_size = os.path.getsize(temp_path)

        if new_size < old_size:
            os.replace(temp_path, filepath)
            print(f"✅ 压缩成功: {os.path.basename(filepath)}  {old_size/1024/1024:.2f}MB → {new_size/1024/1024:.2f}MB")
        else:
            os.remove(temp_path)
            print(f"➡️ 无明显改善: {os.path.basename(filepath)} 保留原图")

    except Exception as e:
        print(f"❌ 压缩失败: {filepath} ({e})")


# === 3. 遍历目录 ===
for filename in os.listdir(img_dir):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    file_path = os.path.join(img_dir, filename)
    size_mb = os.path.getsize(file_path) / 1024 / 1024

    if size_mb > max_size_mb:
        print(f"📉 检测到大图: {filename} ({size_mb:.2f} MB)")
        compress_image(file_path)

print("🎯 全部处理完成。")
