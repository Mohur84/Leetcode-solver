class Solution:
    def partition(self, head, x):
        before=ListNode(0)
        after=ListNode(0)
        beforeTail=before
        afterTail=after
        while head:
            if head.val<x:
                beforeTail.next=head
                beforeTail=beforeTail.next
            else:
                afterTail.next=head
                afterTail=afterTail.next
            head=head.next
        afterTail.next=None
        beforeTail.next=after.next
        return before.next