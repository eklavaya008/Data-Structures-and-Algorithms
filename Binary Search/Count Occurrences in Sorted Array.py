#Solution

def lowerbound(self, nums, target):
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

def upperbound(self, nums, target):
    n = len(nums)
    ub = n
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    return ub

def countFreq(self, nums, target):
    if not nums:
        return [-1, -1]

    lb = self.lowerbound(nums, target)
    if lb == -1 or nums[lb] != target:
        return [-1, -1]

    ub = self.upperbound(nums, target)
    return ub-lb
