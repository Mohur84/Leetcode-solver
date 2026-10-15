class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator=0
        denominator=1
        i=0
        n=len(expression)
        while i<n:
            sign=1
            if expression[i]=='-':
                sign=-1
                i+=1
            elif expression[i]=='+':
                i+=1
            num=0
            while i<n and expression[i].isdigit():
                num=num*10+int(expression[i])
                i+=1
            i+=1
            den=0
            while i<n and expression[i].isdigit():
                den=den*10+int(expression[i])
                i+=1
            num*=sign
            numerator=numerator*den+num*denominator
            denominator*=den
            common=gcd(abs(numerator), denominator)
            numerator//=common
            denominator//=common
        return f"{numerator}/{denominator}"