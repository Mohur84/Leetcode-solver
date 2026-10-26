class Solution:
    def numComponents(self, head: ListNode | None, nums: list[int]) -> int:
        values=set(nums)
        components=0
        previous_included=False
        while head:
            current_included=head.val in values
            if current_included and not previous_included:
                components+=1
            previous_included=current_included
            head=head.next
        return components