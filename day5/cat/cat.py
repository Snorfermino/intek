import re


def promptInput():
    prompting = True
    inputs = []
    while prompting:
        user_inputs = input()
        if user_inputs == " " or user_inputs == "":
            prompting = False
        inputs.append(user_inputs)
    print(inputs)
    for i in range(len(inputs)):
        print(re.sub('[^A-Za-z0-9]+', ' ', inputs[i]))
        l = re.sub('[^A-Za-z0-9]+', ' ', l)
    print(inputs)
    print(' '.join(e for e in inputs if e.isalnum()))

def special_sort(array):
    promptInput()

special_sort([])