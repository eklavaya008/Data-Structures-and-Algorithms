#Solution

def upperbound(arr, x):
    n = len(arr)
    lb = -1
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<=x:
            lb=mid
            low = mid+1
        else:
            high = mid-1    
    return lb

arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
print(upperbound(arr,x))