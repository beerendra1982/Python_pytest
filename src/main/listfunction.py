def minNumber(number):
    min=number[0]
    for i in number:
        if i<min:
            min=i
    return min

def maxNumber(number):
    min=number[0]
    for i in number:
        if i>min:
            min=i
    return min


def evenNumberList(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(even_numbers)
    return even_numbers


