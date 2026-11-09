class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse():
            nonlocal i
            result=set()
            current={""}
            while i<len(expression) and expression[i]!='}':
                if expression[i]==',':
                    result|=current
                    current={""}
                    i+=1
                elif expression[i]=='{':
                    i+=1
                    part=parse()
                    i+=1
                    current={
                        a+b
                        for a in current
                        for b in part
                    }
                else:
                    current={
                        a+expression[i]
                        for a in current
                    }
                    i+=1
            result|=current
            return result
        i=0
        return sorted(parse())