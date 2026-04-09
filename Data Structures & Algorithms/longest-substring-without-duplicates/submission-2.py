class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = deque()
        longest_substring = 0
        for c in s:
            while c in current_substring:
                current_substring.popleft()
            current_substring.append(c)
            longest_substring = max(longest_substring, len(current_substring))
        return longest_substring
        