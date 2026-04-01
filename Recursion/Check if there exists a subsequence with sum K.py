#Solution

def ExistsubseqWSK(index,nums,total,k):
    if total == k:
        return True
    elif total>k:
        return False
    if index >= len(nums):
        return False
    sum = total+nums[index]
    pick = ExistsubseqWSK(index+1,nums,sum,k)
    if pick == True:
        return True
    sum = total
    return ExistsubseqWSK(index+1 ,nums, sum,k)

nums = [5, 9, 4]
k = 9

print(ExistsubseqWSK(0, nums, 0, k))
