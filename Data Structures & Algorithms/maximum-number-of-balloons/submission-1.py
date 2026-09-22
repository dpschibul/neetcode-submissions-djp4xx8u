class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        goal_word = { "b": 1, "a": 1, "l": 2, "o": 2, "n": 1}

        counter = Counter(text)
        res = []
        for c, count in goal_word.items():
            if c not in counter:
                return 0
            res.append(counter[c] // count)
        
        return min(res)

        