class Solution:
    def buildTree(self, inorder, postorder):
        if len(inorder) != len(postorder):
            return None
        hm = {val: idx for idx, val in enumerate(inorder)}
        return self._build(
            inorder, 0, len(inorder) - 1,
            postorder, 0, len(postorder) - 1,
            hm
        )
    def _build(self, inorder, is_, ie, postorder, ps, pe, hm):
        if ps > pe or is_ > ie:
            return None
        root_val = postorder[pe]
        root = TreeNode(root_val)

        inRoot = hm[root_val]
        numsLeft = inRoot - is_
        root.left = self._build(
            inorder, is_, inRoot - 1,
            postorder, ps, ps + numsLeft - 1,
            hm
        )
        root.right = self._build(
            inorder, inRoot + 1, ie,
            postorder, ps + numsLeft, pe - 1,
            hm
        )
        return root