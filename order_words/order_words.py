def order_words(arr):
    resultArr = []
    if not arr:
        return [[]]
    else: 
        for i in arr:
            if sorted(list(filter(lambda a: len(a) == len(i), arr))) not in resultArr:
                resultArr.append(sorted(list(filter(lambda a: len(a) == len(i), arr))))

        return sorted(resultArr, key=lambda x: len(x[0]))
