#Solution

def backtracking(index,total,subset,result,nums):
    if total == 0:
        result.append(subset.copy())
        return 
    if total<0:
        return
    if index>=len(nums):
        return
    for i in range(index,len(nums)):
        if i>index and nums[i] == nums[i-1]:
            continue
        if nums[i] > total:
            break
        subset.append(nums[i])
        sums = total - nums[i]
        backtracking(i+1,sums,subset,result,nums)
        subset.pop()
        
    
def combinationSum2(nums,target):
    nums.sort()
    n = len(nums)
    result = []
    backtracking(0,target,[],result,nums)
    return result


nums = [1,1,2,1,2]
print(combinationSum2(nums,4))
