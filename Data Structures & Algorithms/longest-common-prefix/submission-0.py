class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min([len(s) for s in strs])
        prefix_pos = 0

        while prefix_pos < shortest:
            first = strs[0][prefix_pos]
            for s in strs:
                if s[prefix_pos] != first:
                    return strs[0][0:prefix_pos]


            prefix_pos += 1

        return strs[0][0:prefix_pos]
        