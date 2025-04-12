def validateion(num):
    if num % 3 == 0 and num % 5==0:
        return str(num) + " can be divided by 3 and 5"
    elif num % 3 == 0:
        return str(num) + " can be divided by 3" 
    elif num % 5==0:
        return str(num) + " can be divided by 5" 
    else:
        return str(num) + " can't be divided by 3 or 5"
def quiz():
    try:
        num=input("Enter a input number ")
        msg=validateion(int(num))
        print(msg)
    except Exception as ex:
        print ("Exception :",ex)

