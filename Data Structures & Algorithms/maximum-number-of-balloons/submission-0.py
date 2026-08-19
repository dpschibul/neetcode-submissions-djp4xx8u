class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = "balloon"

        counter = Counter(list(text))

        found_balloon = True
        res = 0

        while found_balloon:
            for c in balloon:
                if c not in counter or counter[c] == 0:
                    found_balloon = False
                    break
                counter[c] -= 1
            if found_balloon:
                res += 1



        return res
        