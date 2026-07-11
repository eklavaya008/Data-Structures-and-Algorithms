class Solution(object):
    def isPalindrome(self, s):
        if s == "":
            return True
        curr_s = s.lower()
        curr_s1 = []
        for ch in curr_s:
            if "a" <= ch <=  "z":
                curr_s1.append(ch)
            elif "0" <= ch <= "9":
                curr_s1.append(ch)
        curr_s2 = "".join(curr_s1)
        i = 0
        j = len(curr_s2) - 1
        while i<j:
            if curr_s2[i] != curr_s2[j]:
                return False
            i+=1
            j-=1
        return True
    
