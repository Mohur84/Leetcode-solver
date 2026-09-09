class Solution(object):
    def buildTree(self, preorder, inorder):
        in_map={val: idx for idx, val in enumerate(inorder)}
        def build(preStart, preEnd, inStart, inEnd):
            if preStart>preEnd or inStart>inEnd:
                return None
            root_val=preorder[preStart]
            root=TreeNode(root_val)
            inRoot=in_map[root_val]
            numsLeft=inRoot-inStart
            root.left=build(preStart+1, preStart+numsLeft, inStart, inRoot-1)
            root.right=build(preStart+numsLeft+1, preEnd, inRoot+1, inEnd)
            return root
        return build(0, len(preorder)-1, 0, len(inorder)-1)
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print root.val,
    printInorder(root.right)