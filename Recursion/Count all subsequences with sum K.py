#Solution

def backtrack(index,total, nums,k):
    if total == k:
        return 1
    if total>k:
        return 0
    if index >= len(nums):
        return 0
    sum = total + nums[index]
    pick = backtrack(index+1,sum,nums,k)
    sum = total
    not_pick = backtrack(index+1,sum,nums,k)
    return pick + not_pick

nums = [5, 9, 4]
k = 9
