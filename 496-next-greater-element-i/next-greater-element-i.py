class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        next_greater={}
        for num in nums2:
            while stack and stack[-1]<num:
                next_greater[stack.pop()]=num
            stack.append(num)
        result=[]
        for num in nums1:
            result.append(next_greater.get(num, -1))
        return result