class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        queue=deque([(root, None)])
        while queue:
            level_size=len(queue)
            parent_x=None
            parent_y=None
            for _ in range(level_size):
                node, parent=queue.popleft()
                if node.val==x:
                    parent_x=parent
                if node.val==y:
                    parent_y=parent
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            if parent_x is not None or parent_y is not None:
                return(
                    parent_x is not None and
                    parent_y is not None and
                    parent_x != parent_y
                )
        return False