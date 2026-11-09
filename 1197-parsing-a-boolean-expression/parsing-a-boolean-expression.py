class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack=[]
        for ch in expression:
            if ch==',':
                continue
            if ch!=')':
                stack.append(ch)
                continue
            values=[]
            while stack and stack[-1]!='(':
                values.append(stack.pop())
            stack.pop()
            operator=stack.pop()
            if operator=='!':
                result=values[0]=='f'
            elif operator=='&':
                result=all(v=='t' for v in values)
            else:
                result=any(v=='t' for v in values)
            stack.append('t' if result else 'f')
        return stack[-1]=='t'