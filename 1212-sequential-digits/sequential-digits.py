class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        result=[]
        digits="123456789"
        for length in range(len(str(low)), len(str(high))+1):
            for i in range(10-length):
                num=int(digits[i:i+length])
                if low<=num<=high:
                    result.append(num)
        return result