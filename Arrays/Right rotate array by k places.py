#Solution

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def rotate(nums, k):
    n = len(nums)
    k = k % n   
    reverse(nums, n - k, n - 1)
    reverse(nums, 0, n - k - 1)
    reverse(nums, 0, n - 1)
    
    return nums

n = [1, 2, 3, 4, 5, 6, 7, 8]
print(rotate(n, 22))