class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        s=str(n)
        m=len(s)
        k=len(digits)
        result=sum(k**length for length in range(1, m))
        for i, ch in enumerate(s):
            smaller=sum(d<ch for d in digits)
            result+=smaller*(k**(m-i-1))
            if ch not in digits:
                return result
        return result+1