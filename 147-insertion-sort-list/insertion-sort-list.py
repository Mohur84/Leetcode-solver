class Solution:
    def insertionSortList(self, head):
        dummy=ListNode(0)
        curr=head
        while curr:
            prev=dummy
            while prev.next and prev.next.val<curr.val:
                prev=prev.next
            nxt=curr.next
            curr.next=prev.next
            prev.next=curr
            curr=nxt
        return dummy.next