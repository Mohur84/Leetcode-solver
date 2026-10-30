class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        result=set()
        current=set()
        for num in arr:
            new_current={num}
            for value in current:
                new_current.add(value|num)
            current=new_current
            result.update(current)
        return len(result)