#Solution

def lowerbound( nums, target):
    n = len(nums)
    lb = -1
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb

def upperbound( nums, target):
    n = len(nums)
    ub = -1
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    return ub

def searchRange( nums, target):
    if not nums:
        return [-1, -1]

    lb = lowerbound(nums, target)
    if lb == -1 or nums[lb] != target:
        return [-1, -1]

    ub = upperbound(nums, target)
    return [lb, ub - 1]

nums = [5,7,7,8,8,10]
target = 7
print(searchRange(nums,target))
