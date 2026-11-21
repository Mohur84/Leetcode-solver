class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        result=0
        while head:
            result=result*2+head.val
            head=head.next
        return result