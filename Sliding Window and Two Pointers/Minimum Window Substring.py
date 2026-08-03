#Solution

class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        dict1 = {}
        dict2 = {}

        for i in range(len(t)):
            dict1[t[i]] = dict1.get(t[i],0)+1

        left = 0
        result = ""
        have = 0
        need = len(dict1)
        
        for right in range(len(s)):
            dict2[s[right]] = dict2.get(s[right],0)+1

            if s[right] in dict1 and dict2[s[right]] == dict1[s[right]]:
                have += 1

            while have == need:
                if result == "" or right - left + 1 < len(result):
                    result = s[left:right+1]

                dict2[s[left]] -= 1

                if s[left] in dict1 and dict2[s[left]] < dict1[s[left]]:
                    have -= 1

                left += 1

        return result
