class Solution(object):
    def frequencySort(self, s):
        result = ""
        char_freq = {}
        for ch in s:
            char_freq[ch] = char_freq.get(ch,0)+1
        sorted_char = sorted(char_freq.items(),key=lambda x:x[1],reverse=True)
        for ch,freq in sorted_char:
            result = result+(ch*freq)
        return result
