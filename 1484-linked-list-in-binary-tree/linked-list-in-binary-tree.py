class Solution:
    def isSubPath(self, head: ListNode | None, root: TreeNode | None) -> bool:
        def match(head, node):
            if head is None:
                return True
            if node is None:
                return False
            if head.val!=node.val:
                return False
            return(
                match(head.next, node.left) or
                match(head.next, node.right)
            )
        def dfs(node):
            if node is None:
                return False
            if match(head, node):
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)