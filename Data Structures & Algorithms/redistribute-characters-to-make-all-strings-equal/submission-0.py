class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = defaultdict(int)

        for word in words:
            for c in word:
                counter[c] += 1
        
        for c, count in counter.items():
            if count % len(words) != 0:
                return False
        return True
        