class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        n=0
        current=head
        while current:
            n+=1
            current=current.next
        part_size=n//k
        extra=n%k
        result=[]
        current=head
        for i in range(k):
            part_head=current
            size=part_size+(1 if i<extra else 0)
            for _ in range(size-1):
                if current:
                    current=current.next
            if current:
                next_part=current.next
                current.next=None
                current=next_part
            result.append(part_head)
        return result