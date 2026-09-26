class Node:
    def __init__(self, key=0, val=0):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self, capacity):
        self.capacity=capacity
        self.cache={}
        self.left=Node()
        self.right=Node()
        self.left.next=self.right
        self.right.prev=self.left
    def remove(self, node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
    def insert(self, node):
        prev=self.right.prev
        prev.next=node
        node.prev=prev
        node.next=self.right
        self.right.prev=node
    def get(self, key):
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key, value)
        self.cache[key]=node
        self.insert(node)
        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]