import os
from PIL import Image, ExifTags

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def resized_img_by_percent(img_file, percent):
    memory = os.path.getsize(img_file) / 1024
    print(f"Картинка {img_file} до сжатия занимает памяти - {toFixed(memory, 2)}КБ")
    print(f"После сжатия: ")
    img = Image.open(img_file)
    (width, height) = img.size
    compr_width = int(width * percent / 100)
    compr_height = int(height * percent / 100)
    compr_img = img.resize((compr_width, compr_height))
    img_name = os.path.basename(img_file)
    compr_img.save(f'resized_img/resized_{percent}%_{img_name}')
    print_info(f"resized_img/resized_{percent}%_{img_name}")

def resized_img_by_memory(img_file, param):
    memory = os.path.getsize(img_file)  # в байтах
    print(f"Картинка {img_file} до сжатия занимает памяти - {toFixed(memory/1024, 2)}КБ")
    print(f"После сжатия: ")
    img = Image.open(img_file)
    (width, height) = img.size
    bit = ((memory * 8) / (width * height))  # memory = width*height * bit
    area = param * 1024 * 8 / bit
    compr_width = int(area / height)
    compr_height = int(area / width)
    compr_img = img.resize((compr_width, compr_height))
    img_name = os.path.basename(img_file)
    compr_img.save(f'resized_img/resized_{param}KB_{img_name}')
    print_info(f"resized_img/resized_{param}KB_{img_name}")


def print_info(file):
    img = Image.open(file)
    (width, height) = img.size
    memory = os.path.getsize(file) / 1024
    img_name = os.path.basename(file)
    print(f"Имя файла - {img_name}")
    print(f"Ширина - {width}px \nВысота - {height}px")
    print(f"Занимает памяти - {toFixed(memory, 2)}КБ\n")


print_info("img/zzz.jpg")
resized_img_by_percent("img/zzz.jpg", 75)  # resize by percent
resized_img_by_memory("img/zzz.jpg", 10)  # resize by memory in KB


