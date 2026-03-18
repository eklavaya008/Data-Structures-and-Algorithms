#Solution

def Swap2no(a,b):
    a = a^b
    b = a^b
    a = a^b
    return [a,b]
