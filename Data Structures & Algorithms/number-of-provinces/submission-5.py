class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v1):
        while v1 != self.parent[v1]:
            self.parent[v1] = self.parent[self.parent[v1]]
            v1 = self.parent[v1]
        return v1

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False

        if p1 > p2:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))

        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if r != c and isConnected[r][c] == 1:
                    uf.union(r, c)
        
        
        parent_set = set()

        for v in range(len(isConnected)):
            parent_set.add(uf.find(v))
        
        return len(parent_set)

                    


        #           city 1 city 2 city 3
        
        # city 1     1
        # city 2             1
        # city 3                     1