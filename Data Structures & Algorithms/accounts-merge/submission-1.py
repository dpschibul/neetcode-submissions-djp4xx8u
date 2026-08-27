class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n1):
        while n1 != self.parent[n1]:
            self.parent[n1] = self.parent[self.parent[n1]]
            n1 = self.parent[n1]
        return n1

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] < self.rank[p2]:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        else:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        adj = {}

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                if email in adj:
                    uf.union(adj[email], i)
                else:
                    adj[email] = i

        groups = defaultdict(set)

        for email, account in adj.items():
            parent = uf.find(account)
            groups[parent].add(email)
        
        res = []

        for parent, emails in groups.items():
            name = accounts[parent][0]
            res.append([name] + sorted(emails))
        
        
        return res

        