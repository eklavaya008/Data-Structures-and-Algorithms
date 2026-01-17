#Solution

def linear_search(nums,x):
    n = len(nums)
    for i in range(0,n):
        if x == nums[i]:
            return i
    return -1
    
n = [1, 2, 3, 4, 5, 6, 7, 8]
print(linear_search(n,6))