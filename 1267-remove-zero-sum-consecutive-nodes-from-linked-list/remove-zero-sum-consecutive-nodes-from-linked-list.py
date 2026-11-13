class Solution:
    def removeZeroSumSublists(self, head: ListNode | None) -> ListNode | None:
        dummy=ListNode(0)
        dummy.next=head
        prefix_sum=0
        last_seen={}
        curr=dummy
        while curr:
            prefix_sum+=curr.val
            last_seen[prefix_sum]=curr
            curr=curr.next
        prefix_sum=0
        curr=dummy
        while curr:
            prefix_sum+=curr.val
            curr.next=last_seen[prefix_sum].next
            curr=curr.next
        return dummy.next