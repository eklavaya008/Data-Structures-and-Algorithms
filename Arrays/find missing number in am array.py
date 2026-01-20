#Solution

def missing_no(nums):
    n = len(nums)
    original_total = (n*(n+1))//2
    return original_total - sum(nums)

n = [3,0,1]
print(missing_no(n))