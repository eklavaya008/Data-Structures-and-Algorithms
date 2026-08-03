#Solution

class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        dict1 = {}
        dict2 = {}
        result = []
        left = 0

        for i in range(len(p)):
            dict1[p[i]] = dict1.get(p[i],0)+1

        for j in range(len(p)):
            dict2[s[j]] = dict2.get(s[j],0)+1
        
        if dict1 == dict2:
            result.append(left)

        for right in range(len(p),len(s)):
            dict2[s[right]] = dict2.get(s[right],0)+1
            dict2[s[left]] -= 1
            if dict2[s[left]] == 0:
                del dict2[s[left]]
            left += 1
            
            if dict1 == dict2:
                result.append(left)

        return result
