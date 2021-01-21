import os
import shutil

my_dir = os.listdir('image')
for image in my_dir:
    if '.jpg' in image:
        image = os.path.join('image', image)
        image_name = image.replace('.jpg', '.png')
        os.rename(image, image_name)
