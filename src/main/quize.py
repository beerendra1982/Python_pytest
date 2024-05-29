def validation(num):
    if num%3==0 and num%5==0:
        return "fizz and lazy"
    elif num%3==0:
        return "fizz"
    elif num%5==0:
        return "lazy"
    else:
        return "not valid number"

def quize():
    try:
        num=input("Enter any number : ")
        msg=validation(int(num))
        print(msg)
    except Exception as ex:
        print("Exception: ", ex)