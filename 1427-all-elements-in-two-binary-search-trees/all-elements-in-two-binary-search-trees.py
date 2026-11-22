class Solution:
    def getAllElements(self, root1: TreeNode | None, root2: TreeNode | None) -> list[int]:
        def inorder(root):
            result=[]
            def dfs(node):
                if not node:
                    return
                dfs(node.left)
                result.append(node.val)
                dfs(node.right)
            dfs(root)
            return result
        list1=inorder(root1)
        list2=inorder(root2)
        i=j=0
        result=[]
        while i<len(list1) and j<len(list2):
            if list1[i]<=list2[j]:
                result.append(list1[i])
                i+=1
            else:
                result.append(list2[j])
                j+=1
        result.extend(list1[i:])
        result.extend(list2[j:])
        return result