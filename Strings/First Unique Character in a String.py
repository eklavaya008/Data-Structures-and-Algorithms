class Solution(object):
    def firstUniqChar(self, s):
        freq_count = {}
        for ch in s:
            freq_count[ch] = freq_count.get(ch,0)+1
        for i in range(len(s)):
            if freq_count[s[i]] == 1:
                return i
        return -1 
