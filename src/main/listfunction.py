def minNumber(number):
    min=number[0]
    for i in number:
        if i<min:
            min=i
    return min