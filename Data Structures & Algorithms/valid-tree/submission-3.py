class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_map = defaultdict(list)

        for edge in edges:
            adj_map[edge[0]].append(edge[1])
            adj_map[edge[1]].append(edge[0])
            

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for adj in adj_map[node]:
                if adj != prev and not dfs(adj, node):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)



        