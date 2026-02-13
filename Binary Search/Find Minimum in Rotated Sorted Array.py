#Solution

def find_min(nums):
    n = len(nums)
    low = 0
    high = n-1
    mini = float("inf")
    while low<=high:
        mid = (low+high)//2
        if nums[mid]<=nums[high]:
            mini =min(mini,nums[mid])
            high = mid -1
        else:
            mini = min(mini,nums[low])
            low = mid +1
    return mini

nums = [3,4,5,1,2]
print(find_min(nums))