class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.cache = {}
        self.tail.next, self.head.prev = self.head, self.tail
        
    # remove node from list
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next 
        next.prev = prev


    # insert node at right
    def insert(self, node):
        temp = self.head.prev
        node.prev = temp
        temp.next = node
        node.next = self.head
        self.head.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.tail.next
            self.remove(lru)
            del self.cache[lru.key]
        
            

                
        
