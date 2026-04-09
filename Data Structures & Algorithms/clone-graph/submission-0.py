class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            copy = Node(node.val)
            visited[node]=copy
            if node.neighbors:
                copy.neighbors = []
            
            for neighbor in node.neighbors:
                if neighbor in visited:
                    copy.neighbors.append(visited[neighbor])
                else:
                    copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node) if node else None
