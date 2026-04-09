class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]
        return cur
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.par[pv] = pu
            self.rank[pv] += self.rank[pu]
        else:
            self.par[pu] = pv
            self.rank[pu] += self.rank[pv]
        return True
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n

        for edge in edges:
            if uf.union(edge[0], edge[1]):
                res -= 1
        return res
