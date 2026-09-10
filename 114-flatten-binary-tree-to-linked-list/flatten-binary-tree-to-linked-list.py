class Solution:
    def flatten(self, root):
        curr=root
        while curr:
            if curr.left:
                pre=curr.left
                while pre.right:
                    pre=pre.right
                pre.right=curr.right
                curr.right=curr.left
                curr.left=None
            curr=curr.right
def print_preorder(root):
    if not root:
        return
    print root.val,
    print_preorder(root.right)
def print_flatten_tree(root):
    if not root:
        return
    print root.val,
    print_faltten_tree(root.right)     