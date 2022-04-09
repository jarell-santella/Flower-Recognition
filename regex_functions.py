import re

# Partition string into 3 parts by regex
def partition_by_regex(pattern, string):
    match = re.search(pattern, string)
    if match is not None:
        partitions = string.partition(match.group(0))
        return partitions[0], partitions[1], partitions[2]
    else:
        return string, '', ''

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