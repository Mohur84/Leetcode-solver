class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        digits=s[1:-1]
        def generate(part):
            result=[]
            n=len(part)
            for i in range(1, n+1):
                integer=part[:i]
                decimal=part[i:]
                if(integer=="0" or not integer.startswith("0")):
                    if not decimal:
                        result.append(integer)
                if decimal:
                    if integer=="0" or not integer.startswith("0"):
                        if not decimal.endswith("0"):
                            result.append(integer+"."+decimal)
            return result
        answer=[]
        for i in range(1, len(digits)):
            left=generate(digits[:i])
            right=generate(digits[i:])
            for x in left:
                for y in right:
                    answer.append(f"({x}, {y})")
        return answer