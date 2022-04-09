import numpy as np
import pandas as pd

import os
import re
from PIL import Image

# Regex for string pattern matching
image_regex = '.*\.jpg$'
daisy_regex = '[a-z| ]*dais[a-z| ]*'
dandelion_regex = '[a-z| ]*dandelion[a-z| ]*'
rose_regex = '[a-z| ]*rose[a-z| ]*'
sunflower_regex = '[a-z| ]*sunflower[a-z| ]*'
tulip_regex = '[a-z| ]*tulip[a-z| ]*'
dir_regex = '({})|({})|({})|({})|({})'.format(daisy_regex,dandelion_regex,rose_regex,sunflower_regex,tulip_regex)
#dir_regex = '(validation)|(test)'

# Lists where directories will be stored of respective flowers
daisy_list, dandelion_list, rose_list, sunflower_list, tulip_list = ([] for i in range(5))
flower_dict = {1: daisy_list, 2: dandelion_list, 3: rose_list, 4: sunflower_list, 5: tulip_list}

# Partition string into 3 parts by regex
def partition_by_regex(regex_search, string):
    partitions = string.partition(regex_search.group(0))
    return (partitions[0], partitions[1], partitions[2])

# Find the first group in regex that matched
def get_regex_group(pattern, string):
    n = re.compile(pattern, re.I).groups
    for i in range(n):
        try:
            if re.search(pattern, string, re.I).group(i+1):
                return i+1
        except:
            return None
    return None

# Resizes an image to square with minimal cropping and no stretching/compressing
def crop_to_square(image, side_length):
    width, height = image.size
    if width > height:
        left = (width-height)/2
        top = 0
        right = width - (width-height)/2
        bottom = height
        image = image.crop((left, top, right, bottom))
    elif width < height:
        left = 0
        top = (height-width)/2
        right = width
        bottom = height - (height-width)/2
        image = image.crop((left, top, right, bottom))
    return image.resize((side_length, side_length), Image.ANTIALIAS)

# Get all image paths from the project directory and store them into their respective lists (works for datasets 1-3)
for root, dirs, files in os.walk('./Datasets/'):
    for file in files:
        if re.search(image_regex, file, re.I):
            n = get_regex_group(dir_regex, root)
            if n is not None:
                image = crop_to_square(Image.open(os.path.join(root, file)), 200)
                flower_dict.get(n).append(image)


#flower_paths = pd.DataFrame({k: pd.Series(v).drop_duplicates() for k, v in flower_dict.items()})

#print(flower_paths[5])