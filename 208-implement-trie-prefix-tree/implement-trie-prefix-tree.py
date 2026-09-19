class Node:
    def __init__(self):
        self.links = {}
        self.flag = False
    def containsKey(self, ch):
        return ch in self.links
    def put(self, ch, node):
        self.links[ch] = node
    def get(self, ch):
        return self.links[ch]
    def setEnd(self):
        self.flag = True
    def isEnd(self):
        return self.flag
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
        node.setEnd()
    def search(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return node.isEnd()
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return True