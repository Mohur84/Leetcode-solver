class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        queue=deque([root])
        leftmost=root.val
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                if i==0:
                    leftmost=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return leftmost