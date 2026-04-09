class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word: str):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()

        for word in words:
            root.addWord(word)

        res, visit = set(), set()

        def dfs(i, j, node, word):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visit or board[i][j] not in node.children:
                return
            
            visit.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.isWord:
                res.add(word)

            dfs(i + 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j - 1, node, word)

            visit.remove((i, j))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)


        


        