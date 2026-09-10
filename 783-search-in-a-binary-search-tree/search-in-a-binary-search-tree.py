class Solution:
    def searchBST(self, root, target):
        while root and root.val!=target:
            if target<root.val:
                root=root.left
            else:
                root=root.right
        return root
root=TreeNode(4)
root.left=TreeNode(2)
root.right=TreeNode(7)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
obj=Solution()
result=obj.searchBST(root, 2)
if result:
    print("Node found:", result.val)
else:
    print("Node not found")