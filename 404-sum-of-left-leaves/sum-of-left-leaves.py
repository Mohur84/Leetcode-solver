class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        total=0
        stack=[(root, False)]
        while stack:
            node, is_left=stack.pop()
            if not node.left and not node.right:
                if is_left:
                    total+=node.val
                continue
            if node.left:
                stack.append((node.left, True))
            if node.right:
                stack.append((node.right, False))
        return total