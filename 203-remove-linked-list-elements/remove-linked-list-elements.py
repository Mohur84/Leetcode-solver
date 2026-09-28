class Solution:
    def removeElements(self, head, val):
        dummy=ListNode(0)
        dummy.next=head
        curr=dummy
        while curr.next:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dummy.next