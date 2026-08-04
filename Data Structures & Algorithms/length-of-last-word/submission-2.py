class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_length = 0

        for i in range(len(s)-1, -1, -1):
            if last_word_length != 0 and s[i] == ' ':
                return last_word_length
            if s[i] != ' ':
                last_word_length += 1
        
        return last_word_length
            
        