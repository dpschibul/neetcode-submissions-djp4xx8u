class UnionFind:

    def __init__(self, n):
        self.par = [n for n in range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        cur = self.par[n]
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]
        return cur
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        
        if self.rank[pu] > self.rank[pv]:
            self.par[pv] = pu
            self.rank[pu] += self.rank[pv]
        else:
            self.par[pu] = pv
            self.rank[pv] += self.rank[pu]
        
        return True

        # par = [2, 2, 2]
        # rank = [1, 1, 3]



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_count = len(isConnected) # 3
        provinces = city_count  # 1
        uf = UnionFind(city_count)

        for i in range(city_count):
            for j in range(city_count):
                if i == j or isConnected[i][j] == 0:
                    continue
                if uf.union(i, j): # 0, 2
                    provinces -= 1
        return provinces

                
                
        #         munich berlin hamburg
        # munich.   1      0       1
        # berlin.   0      1       1
        # hamburg   1      1      1

        # build adjecencymap:
        # {0: [2], 1: [2], 2: [1, 2]}
        