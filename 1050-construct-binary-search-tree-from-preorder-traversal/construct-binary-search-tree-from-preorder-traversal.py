class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        self.index=0
        def build(bound):
            if(self.index==len(preorder) or preorder[self.index]>bound):
                return None
            root_val=preorder[self.index]
            self.index+=1
            root=TreeNode(root_val)
            root.left=build(root_val)
            root.right=build(bound)
            return root
        return build(float('inf'))