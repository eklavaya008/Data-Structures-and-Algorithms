#Solution

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        window = 0
        count = 0

        for i in range(k):
            window += arr[i]
        
        if window >= k * threshold:
                count += 1

        for i in range(k,len(arr)):
            window += arr[i]
            window -= arr[i-k]
            if window >= k * threshold:
                count += 1
        
        return count

