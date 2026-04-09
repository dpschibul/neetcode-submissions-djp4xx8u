class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            char_count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                char_count[index]+=1
            key = tuple(char_count)
            anagrams[key].append(s)

        return list(anagrams.values())