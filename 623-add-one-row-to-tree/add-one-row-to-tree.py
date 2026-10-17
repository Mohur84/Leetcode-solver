class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            new_root=TreeNode(val)
            new_root.left=root
            return new_root
        queue=deque([root])
        level=1
        while queue and level<depth-1:
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        for _ in range(len(queue)):
            node=queue.popleft()
            new_left=TreeNode(val)
            new_left.left=node.left
            node.left=new_left
            new_right=TreeNode(val)
            new_right.right=node.right
            node.right=new_right
        return root