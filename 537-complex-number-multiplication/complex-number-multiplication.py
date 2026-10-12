class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b=map(int, num1[:-1].split('+'))
        c, d=map(int, num2[:-1].split('+'))
        real=a*c-b*d
        imag=a*d+b*c
        return f"{real}+{imag}i"