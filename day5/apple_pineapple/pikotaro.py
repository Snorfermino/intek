def finalString(arr):
    uh = ''
    second = arr[1]
    validFirst = ["pen","apple-pen","apple","long pen"]
    validSecond = ["apple","pineapple","pen","pineapple-pen","apple-pineapple"]
    if arr[0] not in validFirst or arr[1] not in validSecond:
        return -1
    if arr[0] == arr[1] and arr[0] != "pen":
        return -1
    if arr[0] == validFirst[0] and arr[1] not in validSecond[:3]:
        return -1
    if arr[0] == validFirst[1] and arr[1] != validSecond[3]:
        return -1
    if arr[0] == validFirst[2] and arr[1] != validSecond[1]:
        return -1
    if arr[0] == validFirst[3] and arr[1] != validSecond[4]:
        return -1
    first = arr[0]
    cond1 = (arr[0] == "long pen" and arr[1] == "apple-pineapple")
    cond2 = (arr[0] == "apple-pen" and arr[1] == "pineapple-pen")
    if arr[0] == arr[1] == "pen":
        uh = 'Long pen'
    elif cond1 or cond2:
        uh = 'Pen-Pineapple-Apple-Pen'
    else:
        if arr[0] == "pen":
            uh = "{}-{}".format(second.capitalize(), first.capitalize())
        else:
            uh = "{}-{}".format(first.capitalize(),second.capitalize())
    return "I have a {}, I have a {}\nUh! {}!".format(first,second, uh)

def apple_pen(first_ingredient, second_ingredient):
    finalStr = finalString([first_ingredient,second_ingredient])
    if finalStr == -1 :
        raise ValueError('It is not in the lyrics')
    else:
        return finalStr