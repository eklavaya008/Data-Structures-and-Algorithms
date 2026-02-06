#Solution

def getFloorAndCeil(a, x):
    n = len(a)
    floor = -1
    ceil = -1
    low = 0
    high = n-1
    while low<= high:
        mid = (low+high)//2
        if a[mid] == x:
            return [a[mid],a[mid]]
        elif a[mid]>x:
            ceil = a[mid]
            high = mid-1
        else:
            floor = a[mid]
            low = mid+1
    return [floor,ceil]


a=[3, 4, 7, 8, 8, 10]   
x=23
print(getFloorAndCeil(a,x))