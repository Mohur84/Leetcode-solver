class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.pushAll(root)
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    def next(self):
        node = self.stack.pop()
        self.pushAll(node.right)
        return node.val
    def hasNext(self):
        return len(self.stack) > 0