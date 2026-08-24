class Node:

    def __init__(self, key = None, val = None):
        self.prv = None
        self.nxt = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.start, self.end = Node(), Node()
        self.start.nxt, self.end.prv = self.end, self.start
        self.node_map = {}

        
    def append(self, node):
        prev = self.end.prv
        prev.nxt = node
        self.end.prv = node
        node.prv = prev
        node.nxt = self.end


    def remove(self, node_to_remove):
        node_to_remove.prv.nxt, node_to_remove.nxt.prv = node_to_remove.nxt, node_to_remove.prv


    def get(self, key: int) -> int:
        # check if key exists 
        # return value or -1
        # update lru 
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.remove(node)
        self.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.get(key)
            return 

        if self.cap == len(self.node_map):
            lru_node = self.start.nxt
            self.remove(lru_node)
            del self.node_map[lru_node.key]
        new_node = Node(key, value)
        self.node_map[key] = new_node
        self.append(new_node)
        

# put 1, 10
# put 2, 20
# put 4, 30


# {2, 20}
# {4, 30}
# {1, 10}

# [2, 4, 1]
