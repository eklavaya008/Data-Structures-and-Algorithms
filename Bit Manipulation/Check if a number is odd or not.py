#Solution

def odd_even(nums):
    return (nums & 1) == 0

nums = 12
print(odd_even(nums))