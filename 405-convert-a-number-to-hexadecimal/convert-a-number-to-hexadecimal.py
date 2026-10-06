class Solution:
    def toHex(self, num):
        if num==0:
            return "0"
        num &= 0xFFFFFFFF
        digits="0123456789abcdef"
        result=[]
        while num:
            result.append(digits[num & 0xF])
            num>>=4
        return ''.join(reversed(result))