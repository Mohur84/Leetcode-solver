class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow.next
        slow.next=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        first=head
        second=prev
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2