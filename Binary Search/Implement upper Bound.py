#Solution

def upperbound(arr, x):
    n = len(arr)
    ub = n
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>x:
            ub=mid
            high = mid -1
        else:
            low= mid+1    
    return ub

arr = [2,4,6,7]
x = 5
print(upperbound(arr,x))