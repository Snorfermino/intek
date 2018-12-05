from numpy import median
print("Give me a series of numbers and I will give you their median.")
isEmpty = False
inputs = []
while not isEmpty:
    user_inputs = input()
    if not user_inputs.isdigit():
        isEmpty = True
    else:
        inputs.append(int(user_inputs))
if not inputs:
    print("Error, empty dataset")
else:
    print("The median is {}".format(median(inputs)))