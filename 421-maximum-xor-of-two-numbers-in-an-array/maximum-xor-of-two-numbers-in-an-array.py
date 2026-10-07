class Solution:
    def findMaximumXOR(self, nums):
        root={}
        for num in nums:
            node=root
            for bit in range(31, -1, -1):
                b=(num>>bit)&1
                if b not in node:
                    node[b]={}
                node=node[b]
        answer=0
        for num in nums:
            node=root
            current=0
            for bit in range(31, -1, -1):
                b=(num>>bit)&1
                opposite=1-b
                if opposite in node:
                    current|=(1<<bit)
                    node=node[opposite]
                else:
                    node=node[b]
            answer=max(answer, current)
        return answer