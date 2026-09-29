class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        def left_height(node):
            height=0
            while node:
                height+=1
                node=node.left
            return height
        def right_height(node):
            height=0
            while node:
                height+=1
                node=node.right
            return height
        left=left_height(root)
        right=right_height(root)
        if left==right:
            return(1<<left)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)