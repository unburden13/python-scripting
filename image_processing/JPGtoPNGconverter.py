import sys
import os
import pathlib
from PIL import Image

containing_folder = './photos' # sys.argv[1]
new_folder = './pngs' # sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

all_files = os.listdir(containing_folder)

jpg_files = list(filter(lambda file_name: pathlib.Path(file_name).suffix != '.png', all_files))

for jpg_file in jpg_files:
    jpg_image = Image.open(f'{containing_folder}/{jpg_file}')
    jpg_image_name = jpg_file.split(".")[0]
    jpg_image.save(f'{new_folder}/{jpg_image_name}.png', 'png')
