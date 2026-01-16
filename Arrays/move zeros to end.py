#Solution

def move_zeroes(nums):
    if len(nums) == 1:
        return
    i = 0
    while i<len(nums):
        if nums[i] == 0:
            break
        i+=1
    if i == len(nums):
        return
    j = i+1
    while j<len(nums):
        if nums[j] != 0:
            nums[j] , nums[i] = nums[i] , nums[j]
            i+=1
        j+=1