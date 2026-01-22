#Solution

def two_sum(nums,target):
    n = len(nums)
    freq = {}
    for i in range(0,n):
        remaining = target - nums[i]
        if remaining in freq:
            return [freq[remaining],i]
        freq[nums[i]] = i

n = [2,11,7,15]
print(two_sum(n,9))