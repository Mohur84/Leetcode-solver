class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        queue=deque([root])
        found_null=False
        while queue:
            node=queue.popleft()
            if node is None:
                found_null=True
            else:
                if found_null:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True