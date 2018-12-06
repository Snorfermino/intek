import itertools
from collections import defaultdict


def generate_autocomplete(words):
    charSet = set()
    finaldict = defaultdict(list)
    wordsUq = list(set(words))
    for w in words:
        for i in range(len(list(w))):
            charSet.add(w[i])
    for L in range(1,len(list(charSet))):
        for subset in itertools.permutations(''.join(list(charSet)), L):
            subsetInStr = ''.join(subset)
            for w in wordsUq:
                if w.startswith(subsetInStr) and w not in finaldict[subsetInStr]:
                    finaldict[subsetInStr].append(w)
    return dict(finaldict)