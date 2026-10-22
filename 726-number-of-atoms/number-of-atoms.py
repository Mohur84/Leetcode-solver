class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack=[Counter()]
        i=0
        n=len(formula)
        while i<n:
            if formula[i]=='(':
                stack.append(Counter())
                i+=1
            elif formula[i]==')':
                i+=1
                start=i
                while i<n and formula[i].isdigit():
                    i+=1
                multiplier=int(formula[start:i]) if start<i else 1
                group=stack.pop()
                for atom, count in group.items():
                    stack[-1][atom]+=count*multiplier
            else:
                start=i
                i+=1
                while i<n and formula[i].islower():
                    i+=1
                atom=formula[start:i]
                start=i
                while i<n and formula[i].isdigit():
                    i+=1
                count=int(formula[start:i]) if start<i else 1
                stack[-1][atom]+=count
        result=[]
        for atom in sorted(stack[-1]):
            result.append(atom)
            count=stack[-1][atom]
            if count>1:
                result.append(str(count))
        return ''.join(result)