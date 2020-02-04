import os
from PIL import Image, ExifTags
from hw16 import get_location

img_folder = r"img"
img_contents = os.listdir(img_folder)
for image in img_contents:
    full_path = os.path.join(img_folder,image)
    pil_img = Image.open(full_path)
    if pil_img._getexif() != None:
        exif = {ExifTags.TAGS[k]: v for k, v in pil_img._getexif().items() if k in ExifTags.TAGS }
        if 'GPSInfo' in exif:
            print(f"GPS информация по фотографии {image} :")
            Latitude = str(exif['GPSInfo'][2]).strip("()")
            Latitude = Latitude.split(",")[0] + '.' + Latitude.split(",")[2].strip(" (")
            Longitude = str(exif['GPSInfo'][4]).strip("()")
            Longitude = Longitude.split(",")[0] + '.' + Longitude.split(",")[2].strip(" (")
            get_location(Latitude, Longitude)
        else:
            print(f"В фотографии {image} нет GPS данных \n")
