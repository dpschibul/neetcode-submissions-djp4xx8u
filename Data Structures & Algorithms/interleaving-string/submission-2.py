class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            k = i + j
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j):
                    memo[(i, j)] = True
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1):
                    memo[(i, j)] = True
                    return True

            memo[(i, j)] = False
            return False

        return dfs(0, 0)