import os

# === 1. 配置 ===
# 图片目录（改成你的路径）
img_dir = r"F:\Hexo\source\images\gallery"
img_dir = r"F:\Hexo\source\images\pet"
# 图片文件扩展名（可按需增加）
exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.JPG', '.PNG')

# === 2. 扫描目录 ===
images = [f for f in os.listdir(img_dir) if f.endswith(exts)]
images.sort()  # 可去掉这行让顺序随机

# === 3. 生成 HTML 内容 ===
template = """
<div class="gallery-random">
{}
</div>
"""

item_htmls = []
for img in images:
    if img_dir == r"F:\Hexo\source\images\gallery":
      path = f"/images/gallery/{img}"
    else:
       path = f"/images/pet/{img}"
    item_htmls.append(f'''  <a class="gallery-item" data-fancybox="gallery" href="{path}">
    <img src="{path}" alt="">
  </a>''')

body = template.format("\n".join(item_htmls))

# === 4. 生成 Markdown 输出 ===
md_header = """---
title: 照片墙
date: 2025-11-04
layout: page
comments: false
---

<style>
.gallery-random {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  padding: 10px;
}
.gallery-item {
  flex: 1 1 calc(30% - 12px);
  max-width: 320px;
  border-radius: 10px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.gallery-item:nth-child(3n) {
  flex: 1 1 calc(25% - 12px);
}
.gallery-item:nth-child(4n) {
  flex: 1 1 calc(35% - 12px);
}
.gallery-item:nth-child(5n) {
  flex: 1 1 calc(28% - 12px);
}
.gallery-item img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 10px;
  object-fit: cover;
  transition: transform 0.3s ease;
}
.gallery-item:hover {
  transform: scale(1.03);
  box-shadow: 0 5px 15px rgba(0,0,0,0.25);
}
@media (max-width: 900px) {
  .gallery-item { flex: 1 1 calc(45% - 12px); }
}
@media (max-width: 600px) {
  .gallery-item { flex: 1 1 100%; }
}
</style>
"""

md_content =  body

# === 5. 输出 ===
output_path = os.path.join(os.getcwd(), "index_gallery.md")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"✅ 生成完成：{output_path}")
print(f"包含 {len(images)} 张图片。")
