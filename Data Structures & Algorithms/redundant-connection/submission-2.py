class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        def find(n):
            if n == parent[n]:
                return parent[n]

            parent[n] = find(parent[n])
            return parent[n]

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = parent[p1]
                rank[p1] += 1
            else:
                parent[p1] = parent[p2]
                rank[p2] += 1
            return True
            
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        
        return []