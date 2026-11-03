from fractions import Fraction
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert(num):
            if '(' not in num:
                return Fraction(num)
            integer, decimal=num.split('.')
            non_repeat, repeat=decimal.split('(')
            repeat=repeat[:-1]
            result=Fraction(int(integer), 1)
            if non_repeat:
                result+=Fraction(int(non_repeat), 10**len(non_repeat))
            if repeat:
                result+=Fraction(
                    int(repeat),
                    10**len(non_repeat)*(10**len(repeat)-1)
                )
            return result
        return convert(s)==convert(t)
from fractions import Fraction
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert(num):
            if '(' not in num:
                return Fraction(num)
            integer, decimal = num.split('.')
            non_repeat, repeat = decimal.split('(')
            repeat = repeat[:-1]
            result = Fraction(int(integer), 1)
            if non_repeat:
                result += Fraction(int(non_repeat), 10 ** len(non_repeat))
            if repeat:
                result += Fraction(
                    int(repeat),
                    10 ** len(non_repeat) * (10 ** len(repeat) - 1)
                )
            return result
        return convert(s) == convert(t)