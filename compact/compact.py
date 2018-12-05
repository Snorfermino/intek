def compact(array):
    for a in array:
        if a == None:
            array.remove(a)
    return array
    