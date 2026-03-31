#Solution

def printsubseqWSK(index,subset,nums,total,k,result):
    if total == k:
        result.append(subset.copy())
        return
    elif total>= k:
        return 
    if index>=len(nums):
        return
    subset.append(nums[index])
    total = total+nums[index]
    printsubseqWSK(index+1,subset,nums,total,k,result)
    e = subset.pop()
    total -= e
    printsubseqWSK(index+1,subset,nums,total,k,result)

result = []
printsubseqWSK(0,[],[5,9,4],0,9,result)
print(result)

