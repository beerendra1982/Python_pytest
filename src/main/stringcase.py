
def to_camel_case(text):
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + ''.join(i.capitalize() for i in s[1:])

def isBlank(myString):
    return not (myString and myString.strip())

def upper(txt):
    return txt.upper()
