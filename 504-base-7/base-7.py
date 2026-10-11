class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        sign="-" if num<0 else ""
        num=abs(num)
        result=""
        while num>0:
            result=str(num%7)+result
            num//=7
        return sign+result