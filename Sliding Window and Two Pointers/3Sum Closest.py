#Solution

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n-2):

            k = i+1
            j = n-1

            while k < j:
                total_sum = nums[i] + nums[k] + nums[j]

                if abs(total_sum - target) < abs(closest - target):
                    closest = total_sum
                
                if total_sum == target:
                    return target

                elif total_sum < target:
                    k += 1
                else:
                    j -= 1

        return closest
