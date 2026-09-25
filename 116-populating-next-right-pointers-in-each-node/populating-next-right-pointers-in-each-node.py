class Solution:
    def connect(self, root):
        if not root:
            return None
        leftmost=root
        while leftmost.left:
            head=leftmost
            while head:
                head.left.next=head.right
                if head.next:
                    head.right.next = head.next.left
                head=head.next
            leftmost=leftmost.left
        return root
