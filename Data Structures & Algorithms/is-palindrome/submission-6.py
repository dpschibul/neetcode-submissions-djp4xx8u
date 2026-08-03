class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if not self.isAlphaNum(s[left]):
                left += 1
                continue
            if not self.isAlphaNum(s[right]):
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True
    
    def isAlphaNum(self, c) -> bool:
        if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'):
            return True
        return False
        