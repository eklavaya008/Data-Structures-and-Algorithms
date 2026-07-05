class Solution(object):
    def romanToInt(self, s):
        dic_letter = {
             "I":1,
             "V":5,
             "X":10,
             "L":50,
             "C":100,
             "D":500,
             "M":1000
        }
        n = len(s)
        result = 0
        for i in range(n):
            if i < n-1 and dic_letter[s[i]] < dic_letter[s[i+1]]:
                result -= dic_letter[s[i]]
            else:
                result+= dic_letter[s[i]]
        return result

