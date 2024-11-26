from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# 获取文件夹中的所有图片文件
def get_image_files(folder_path):
    image_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".jpg") or file.endswith(".png"):
            image_files.append(os.path.join(folder_path, file))
    return image_files

# 将图片合并成一个pdf文档
def images_to_pdf(images, pdf_file):
    c = canvas.Canvas(pdf_file, pagesize=letter)
    for image in images:
        c.drawImage(image, 0, 0, width=letter[0], height=letter[1])
        c.showPage()
    c.save()

# 将文件夹中的所有图片合并成一个pdf文档
def merge_images_to_pdf(folder_path, pdf_file):
    image_files = get_image_files(folder_path)
    images_to_pdf(image_files, pdf_file)

# 示例用法
folder_path = 'D:\\downloaded_images'
pdf_file = folder_path + '\\' + 'output.pdf'
merge_images_to_pdf(folder_path, pdf_file)
