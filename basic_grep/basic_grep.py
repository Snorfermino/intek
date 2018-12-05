def basic_grep(text, string):
    stringArray = text.split("\n")
    arrayString = list(string)
    removeIndexes = []
    for i in range(len(arrayString)):
        if not arrayString[i].isalpha():
            removeIndexes.append(i)

    for x in range(len(removeIndexes)):
        arrayString[removeIndexes[x]] = " "
    editString = "".join(arrayString)

    for y in stringArray:
        if y.find(editString) == -1:
            print(y)
            stringArray.remove(y)
            
    print(editString)
    print(stringArray)



basic_grep("Hellow\nPotato\nMellow", "ow$23232")