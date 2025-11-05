import os

# === 1. 配置 ===

img_dir_list = [
r"F:\Hexo\source\images\gallery",
r"F:\Hexo\source\images\food",
r"F:\Hexo\source\images\pet",
r"F:\Hexo\source\images\daily"
]

# 对应网页路径（注意 / 而不是 \）

path_list = [
"/images/gallery/",
"/images/food/",
"/images/pet/",
"/images/daily/"
]

# 图片文件扩展名

exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.JPG', '.PNG')

# === 2. 准备输出文件 ===

output_path = os.path.join(os.getcwd(), "all_images.md")

with open(output_path, "w", encoding="utf-8") as f_out:
  for img_dir, web_path in zip(img_dir_list, path_list):
      # 扫描目录
      images = [f for f in os.listdir(img_dir) if f.endswith(exts)]
      images.sort()

      if not images:
          continue

      # 写目录分隔和标题
      category_name = os.path.basename(img_dir)
      f_out.write(f"\n---\n\n### {category_name}\n\n")

      # 生成 HTML
      f_out.write('<div class="gallery-random">\n')
      for img in images:
          f_out.write(f'  <a class="gallery-item" data-fancybox="gallery" href="{web_path}{img}">\n')
          f_out.write(f'    <img src="{web_path}{img}" alt="">\n')
          f_out.write('  </a>\n')
      f_out.write('</div>\n')

print(f"✅ 生成完成：{output_path}")
