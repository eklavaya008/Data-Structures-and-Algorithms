#Solution

def second_large(nums):
    largest = float("-inf")
    S_largest = float("-inf")
    n = len(nums)
    for i in range(0,n):
        largest = max(largest,nums[i])
    for i in range(0,n):
        if nums[i]>S_largest and nums[i]!=largest:
            S_largest = nums[i]
    return S_largest
    

n = [3,4,1,7,9,10]
print(second_large(n))