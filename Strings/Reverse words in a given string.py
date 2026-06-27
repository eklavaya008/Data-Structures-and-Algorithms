class Solution(object):
    def reverseWords(self, s):
        words = []
        current_word = ""

        for ch in s:
            if ch != " ":
                current_word += ch
            else:
                if current_word:
                    words.append(current_word)
                    current_word = ""
        if current_word:
            words.append(current_word)
        
        words.reverse()

        return " ".join(words)

