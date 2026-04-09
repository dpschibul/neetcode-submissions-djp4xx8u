class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set()
        count = 0
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for a in adj[node]:
                dfs(a)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1

        return count
