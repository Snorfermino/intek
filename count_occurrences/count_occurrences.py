from collections import Counter
from collections import defaultdict


def count_occurrences(string):
    arrStr = string.split()
    v = defaultdict(list)
    for key, value in sorted(Counter(arrStr).items()):
        v[value].append(key)

    return dict(v)