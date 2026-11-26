class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        digits.sort(reverse=True)
        remainder=sum(digits)%3
        rem1=[d for d in digits if d%3==1]
        rem2=[d for d in digits if d%3==2]
        if remainder==1:
            if rem1:
                digits.remove(rem1[-1])
            else:
                if len(rem2)<2:
                    return ""
                digits.remove(rem2[-1])
                digits.remove(rem2[-2])
        elif remainder==2:
            if rem2:
                digits.remove(rem2[-1])
            else:
                if len(rem1)<2:
                    return ""
                digits.remove(rem1[-1])
                digits.remove(rem1[-1])
        if not digits:
            return ""
        if digits[0]==0:
            return "0"
        return ''.join(map(str, digits))