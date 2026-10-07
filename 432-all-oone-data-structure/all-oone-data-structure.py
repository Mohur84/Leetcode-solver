class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None
class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_node = {}
    def _insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def inc(self, key):
        if key not in self.key_node:
            if self.head.next != self.tail and self.head.next.count == 1:
                node = self.head.next
            else:
                node = Node(1)
                self._insert_after(self.head, node)
            node.keys.add(key)
            self.key_node[key] = node
        else:
            current = self.key_node[key]
            new_count = current.count + 1
            if current.next != self.tail and current.next.count == new_count:
                node = current.next
            else:
                node = Node(new_count)
                self._insert_after(current, node)
            node.keys.add(key)
            self.key_node[key] = node
            current.keys.remove(key)
            if not current.keys:
                self._remove_node(current)
    def dec(self, key):
        current = self.key_node[key]
        if current.count == 1:
            del self.key_node[key]
        else:
            new_count = current.count - 1
            if current.prev != self.head and current.prev.count == new_count:
                node = current.prev
            else:
                node = Node(new_count)
                self._insert_after(current.prev, node)
            node.keys.add(key)
            self.key_node[key] = node
        current.keys.remove(key)
        if not current.keys:
            self._remove_node(current)
    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))
    def getMinKey(self):
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))