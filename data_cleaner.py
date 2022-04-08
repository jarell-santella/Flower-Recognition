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
daisies, dandelions, roses, sunflowers, tulips = ([] for i in range(5))

# Partition string into 3 parts by regex
def partition_by_regex(regex_search, string):
    partitions = string.partition(regex_search.group(0))
    return (partitions[0], partitions[1], partitions[2])

# Look in entire project directory for folders of the 5 types of flowers
for root, dir, files in os.walk('./'):
    regex_search = re.search(dir_regex, root, re.I)
    if regex_search:
        root_components = partition_by_regex(regex_search, root)
        print(os.path.join(root_components[0],root_components[1]))
        