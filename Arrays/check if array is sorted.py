#Solution

def check_sort(nums):
    n = len(nums)
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True

n = [3,4,1,7,9,10,14]
print(check_sort(n))