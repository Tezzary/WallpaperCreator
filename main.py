#import pillow
from PIL import Image
import os

monitors = [[3840, 2160], [2560, 1440], [1920, 1080]]
            
image = "mountainwallpaper.jpg"

image = Image.open(image)

image_width, image_height = image.size

largest_x = 0
largest_y = 0

for monitor in monitors:
    if monitor[0] > largest_x:
        largest_x = monitor[0]
    if monitor[1] > largest_y:
        largest_y = monitor[1]
crop_x = len(monitors) * largest_x
crop_y = largest_y

anchor = "bottom"

if anchor == "center":
    start_x = (image_width - crop_x) // 2
    start_y = (image_height - crop_y) // 2

elif anchor == "bottom":
    start_x = (image_width - crop_x) // 2
    start_y = image_height - crop_y


folder = "croppedimages"

if not os.path.exists(folder):
    os.makedirs(folder)

os.chdir(folder)

for i in range(len(monitors)):
    cropped_image = image.crop((start_x + largest_x * i, start_y, start_x + largest_x * (i + 1), crop_y + start_y))

    cropped_image.save(f"cropped_image_{i}.jpg")