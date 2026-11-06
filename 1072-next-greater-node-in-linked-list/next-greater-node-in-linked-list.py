class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:
        values=[]
        while head:
            values.append(head.val)
            head=head.next
        result=[0]*len(values)
        stack=[]
        for i in range(len(values)):
            while stack and values[i]>values[stack[-1]]:
                index=stack.pop()
                result[index]=values[i]
            stack.append(i)
        return result