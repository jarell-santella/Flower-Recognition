import re

# Partition string into 3 parts by regex
def partition_by_regex(pattern, string):
    match = re.search(pattern, string, re.I)
    if match:
        partitions = string.partition(match.group(0))
        return partitions[0], partitions[1], partitions[2]
    else:
        return string, '', ''

# Find the first group in regex that matched
def get_regex_group(pattern, string, num=True):
    match = re.search(pattern, string, re.I)
    if match:
        n = re.compile(pattern, re.I).groups
        for i in range(n):
            if match.group(i+1):
                if num:
                    return i+1
                else:
                    return match.group(0)
    else:
        return None