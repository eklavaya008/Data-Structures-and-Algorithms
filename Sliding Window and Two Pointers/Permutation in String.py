#Solution

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        my_dict1 = {}
        my_dict2 = {}

        for i in range(len(s1)):
            my_dict1[s1[i]] = my_dict1.get(s1[i],0) + 1

        for j in range(len(s1)):
            my_dict2[s2[j]] = my_dict2.get(s2[j],0) + 1
        
        if my_dict1 == my_dict2:
            return True
        
        left = 0
        for right in range(len(s1),len(s2)):
            my_dict2[s2[right]] = my_dict2.get(s2[right],0)+1

            my_dict2[s2[left]] -= 1
            if my_dict2[s2[left]] == 0:
                del my_dict2[s2[left]]
            left += 1
            
            if my_dict1 == my_dict2:
                return True
        
        return False
