class Solution(object):
    def lengthOfLastWord(self, s):
        word = []
        curr_word = ""
        for ch in s:
            if ch != " ":
                curr_word+=ch
            else:
                if curr_word:
                    word.append(curr_word)
                    curr_word = ""
        if curr_word:
            word.append(curr_word)
        result = len(word[-1])
        return result
    
