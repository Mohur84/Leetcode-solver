class CBTInserter:
    def __init__(self, root: TreeNode | None):
        self.root=root
        self.queue=deque()
        q=deque([root])
        while q:
            node=q.popleft()
            if not node.left or not node.right:
                self.queue.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    def insert(self, val: int) -> int:
        parent=self.queue[0]
        new_node=TreeNode(val)
        if not parent.left:
            parent.left=new_node
        else:
            parent.right=new_node
            self.queue.popleft()
        self.queue.append(new_node)
        return parent.val
    def get_root(self) -> TreeNode | None:
        return self.root