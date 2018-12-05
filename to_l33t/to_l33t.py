import re
def to_l33t(string):
    result = re.compile(re.escape('a'), re.IGNORECASE).sub('4',string)
    result = re.compile(re.escape('e'), re.IGNORECASE).sub('3',result)
    result = re.compile(re.escape('i'), re.IGNORECASE).sub('1',result)
    result = re.compile(re.escape('o'), re.IGNORECASE).sub('0',result)
    result = re.compile(re.escape('u'), re.IGNORECASE).sub('8',result)
    return result