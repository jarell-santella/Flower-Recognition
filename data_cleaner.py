import numpy as np
import pandas as pd

import os
import re

from PIL import Image
import imagehash

from regex_functions import get_regex_group

# Regex for string pattern matching
image_regex = '.*\.jpg$'
daisy_regex = '[a-z| ]*dais[a-z| ]*'
dandelion_regex = '[a-z| ]*dandelion[a-z| ]*'
rose_regex = '[a-z| ]*rose[a-z| ]*'
sunflower_regex = '[a-z| ]*sunflower[a-z| ]*'
tulip_regex = '[a-z| ]*tulip[a-z| ]*'
dir_regex = '({})|({})|({})|({})|({})'.format(daisy_regex,dandelion_regex,rose_regex,sunflower_regex,tulip_regex)

# Dataframe of pixel data of images with labels indicating which type of flower the pixel data is for
flower_data = pd.DataFrame(columns=['data', 'hash', 'label'])

# Resizes an image to square with minimal cropping and no stretching/compressing
def crop_to_square(image, side_length=100):
    width, height = image.size
    if width > height:
        left = (width-height)/2
        top = 0
        right = width-(width-height)/2
        bottom = height
        image = image.crop((left, top, right, bottom))
    elif width < height:
        left = 0
        top = (height-width)/2
        right = width
        bottom = height-(height-width)/2
        image = image.crop((left, top, right, bottom))
    return image.resize((side_length, side_length), Image.ANTIALIAS)

def hash_image(image, hashing_function=imagehash.average_hash, hash_size=10):
    image = crop_to_square(image, hash_size)
    return hashing_function(image)

def main():
    # Get all image paths from the project directory and store them into their respective lists
    global flower_data

    for root, dirs, files in os.walk('./Datasets/'):
        for file in files:
            if re.search(image_regex, file, re.I):
                n = get_regex_group(dir_regex, root)
                if n is not None:
                    image = crop_to_square(Image.open(os.path.join(root, file)), 200)
                    pixel_data = np.asarray(image)
                    hash_value = hash_image(image, hash_size=8)
                    row_data = pd.Series([pixel_data, hash_value, n], index=flower_data.columns)
                    flower_data = flower_data.append(row_data, ignore_index=True)

    flower_data = flower_data.drop_duplicates('hash')
    flower_data = flower_data[['data', 'label']]

    flower_data.to_pickle('flower_data.pkl')

if __name__ == "__main__":
    main()