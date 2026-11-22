class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        queue=deque([root])
        total=0
        while queue:
            total=0
            for _ in range(len(queue)):
                node=queue.popleft()
                total+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return total