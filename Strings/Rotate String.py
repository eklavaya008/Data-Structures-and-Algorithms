class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        super_s = s+s
        if goal in super_s:
            return True
        return False
    
