class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        q=deque([(root, 1)])
        while q:
            node, depth=q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))