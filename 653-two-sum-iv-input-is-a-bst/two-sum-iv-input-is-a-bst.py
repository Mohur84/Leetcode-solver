class BSTIterator:
    def __init__(self, root, isReverse):
        self.stack = []
        self.reverse = isReverse
        self.pushAll(root)
    def hasNext(self):
        return len(self.stack) > 0
    def next(self):
        node = self.stack.pop()

        if self.reverse:
            self.pushAll(node.left)
        else:
            self.pushAll(node.right)
        return node.val
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            if self.reverse:
                node = node.right
            else:
                node = node.left
class Solution:
    def findTarget(self, root, k):
        if not root:
            return False
        left = BSTIterator(root, False)
        right = BSTIterator(root, True)
        i = left.next()
        j = right.next()
        while i < j:
            if i + j == k:
                return True
            elif i + j < k:
                if left.hasNext():
                    i = left.next()
                else:
                    break
            else:
                if right.hasNext():
                    j = right.next()
                else:
                    break
        return False