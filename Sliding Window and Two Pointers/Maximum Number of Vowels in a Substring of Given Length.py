#Solution

class Solution(object):
    def maxVowels(self, s, k):
        window = 0

        for i in range(k):
            if s[i] in 'aeiou':
                window += 1
        
        ans = window

        for i in range(k,len(s)):
            if s[i] in 'aeiou':
                window += 1
            if s[i-k] in 'aeiou':
                window -= 1
            ans = max(ans,window)
        
        return ans

