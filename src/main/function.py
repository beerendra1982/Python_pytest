def average(a,b):
    print("Average of two number is : ", (a+b)/2)
    return (a+b)/2

def addition(a,b):
    return a+b


def sumOfNumber(*args):
    sum=0
    for i in args:
        sum =sum +i
    return sum