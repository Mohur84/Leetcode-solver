class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen=set()
        for num in arr:
            if num*2 in seen:
                return True
            if num%2==0 and num//2 in seen:
                return True
            seen.add(num)
        return False