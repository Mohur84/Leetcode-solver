class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        result=[]
        prev=None
        count=0
        max_count=0
        def inorder(node):
            nonlocal prev, count, max_count
            if not node:
                return
            inorder(node.left)
            if node.val==prev:
                count+=1
            else:
                prev=node.val
                count=1
            if count>max_count:
                max_count=count
                result.clear()
                result.append(node.val)
            elif count==max_count:
                result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result