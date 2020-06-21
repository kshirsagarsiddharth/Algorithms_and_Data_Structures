import collections
from collections import Counter
def first_count(s):
    count = collections.Counter(s)
    for idx,ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1