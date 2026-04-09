class TreeNode:
    def __init__(self, value):
        self.value: str = value
        self.children: [TreeNode] = []
        self.is_leaf: bool = False

    def get_child(self, val: str) -> TreeNode | None:
        for child in self.children:
            if child.value == val:
                return child
        return None

class PrefixTree:

    def __init__(self):
        self.head = TreeNode('')
        

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            child = curr.get_child(c)
            if child:
                curr = child
            else:
                c_node = TreeNode(c)
                curr.children.append(c_node)
                curr = c_node 
        curr.is_leaf = True


    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            c_child = curr.get_child(c)
            if not c_child:
                return False
            curr = c_child

        return curr.is_leaf


        

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            c_child = curr.get_child(c)
            if not c_child:
                return False
            curr = c_child

        return True
        


        