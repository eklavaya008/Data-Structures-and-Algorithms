#Solution

class Solution(object):
    def characterReplacement(self, s, k):
        left = 0 
        result = 0
        my_dict = {}
        max_freq = 0

        for right in range(len(s)):
            my_dict[s[right]] = my_dict.get(s[right],0) + 1
            max_freq = max(max_freq,my_dict[s[right]])

            while (right-left+1) - max_freq > k:
                my_dict[s[left]] -= 1
                left += 1

            result = max(result,right-left+1)

        return result
