from collections import defaultdict


def bdmi(dic):
    v = defaultdict(list)
    for key, _ in sorted(dic.items()):
        tempArr = dic[key]
        for i in tempArr:
            v[i].append(key)
    return dict(v)