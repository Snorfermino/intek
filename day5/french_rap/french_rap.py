from collections import defaultdict


def french_rap(csv):
    filename = csv + ".csv"
    finaldict = defaultdict(list)
    try:
        f = open(filename,'r')
        fileContents =  f.read()
        arrContents = fileContents.split("\n")
        for arr in arrContents:
            pair = arr.split(',')
            key = pair[1]
            value = pair[0]
            finaldict[key].append(value)
        return dict(finaldict)
    except FileNotFoundError:
        raise FileNotFoundError('File does not exist')