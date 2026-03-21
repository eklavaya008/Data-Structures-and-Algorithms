#Solution

def singlenumber(nums):
    ans = 0
    for i in nums:
        ans = ans^i
    return i

