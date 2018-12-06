from collections import defaultdict


def merge_dict(dictionaries):
    mergedDict = defaultdict(list)
    for i in range(len(dictionaries)):
        for key,value in sorted(dictionaries[i].items()):
            mergedDict[key].append(value)
    return dict(mergedDict)