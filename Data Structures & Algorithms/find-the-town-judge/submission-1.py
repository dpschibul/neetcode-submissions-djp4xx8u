class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = defaultdict(set)
        trusts = defaultdict(set)
        
        for t in trust:
            trusted_by[t[1]].add(t[0])
            trusts[t[0]].add(t[1])

        print(trusts)
        print(trusted_by)
        for i in range(1, n+1):
            if not i in trusts and len(trusted_by[i]) == n-1:
                return i

        return -1
        