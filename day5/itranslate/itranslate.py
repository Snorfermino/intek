def itranslate(dic, string):
    arrStr = string.split()
    finalArr = []
    try:
        for w in arrStr:
            finalArr.append(dic[w])
    except KeyError:
        raise KeyError('Missing word')
    return ' '.join(finalArr)
