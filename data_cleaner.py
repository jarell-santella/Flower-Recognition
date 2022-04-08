import numpy as np
import pandas as pd

import sys
import os
import re
import PIL
import glob

# Regex for string pattern matching
# file_regex = re.compile('.*\.jpg')
daisy_regex = '[a-z| ]*dais[a-z| ]*'
dandelion_regex = '[a-z| ]*dandelion[a-z| ]*'
rose_regex = '[a-z| ]*rose[a-z| ]*'
sunflower_regex = '[a-z| ]*sunflower[a-z| ]*'
tulip_regex = '[a-z| ]*tulip[a-z| ]*'
dir_regex = '({})|({})|({})|({})|({})'.format(daisy_regex,dandelion_regex,rose_regex,sunflower_regex,tulip_regex)
#dir_regex = '(validation)|(test)'

# Lists where directories will be stored of respective flowers
daisy_dir, dandelion_dir, rose_dir, sunflower_dir, tulip_dir = ([] for i in range(5))
flower_dict = {1: daisy_dir, 2: dandelion_dir, 3: rose_dir, 4: sunflower_dir, 5: tulip_dir}

# Partition string into 3 parts by regex
def partition_by_regex(regex_search, string):
    partitions = string.partition(regex_search.group(0))
    return (partitions[0], partitions[1], partitions[2])

# Find the first group in regex that matched
def get_regex_group(pattern, string):
    n = re.compile(pattern, re.I).groups
    for i in range(n):
        if re.search(pattern, string, re.I).group(i+1):
            return i+1
    return None

#for root, dirs, files in os.walk('./Datasets'):
#    regex_search = re.search(dir_regex, root, re.I)
#    print(root)
#    if regex_search:
#        root_components = partition_by_regex(regex_search, root)
#        n = get_regex_group(dir_regex, root_components[1])
#        flower_dict.get(n).append(os.path.join(root_components[0],root_components[1]))
#
#        print(os.path.join(root_components[0],root_components[1]))
#        print(root_components[1] + str(get_regex_group(dir_regex, root_components[1])))

# Look in entire project directory for folders of the 5 types of flowers
for root, dirs, files in os.walk('./Datasets'):
    for dir in dirs:
        regex_search = re.search(dir_regex, dir, re.I)
        if regex_search:
            n = get_regex_group(dir_regex, dir)
            flower_dict.get(n).append(os.path.join(root,dir))
