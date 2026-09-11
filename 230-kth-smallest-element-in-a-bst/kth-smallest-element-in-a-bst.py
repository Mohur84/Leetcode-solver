class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.result = None
        self.inorder(root)
        return self.result
    def inorder(self, node):
        if node is None or self.result is not None:
            return
        self.inorder(node.left)
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        self.inorder(node.right)
  