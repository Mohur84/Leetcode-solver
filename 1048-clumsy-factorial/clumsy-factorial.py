class Solution:
    def clumsy(self, n: int) -> int:
        stack=[n]
        n-=1
        operations=['*','/','+','-']
        i=0
        while n>0:
            op=operations[i%4]
            if op=='*':
                stack[-1]*=n
            elif op=='/':
                stack[-1]=int(stack[-1]/n)
            elif op=='+':
                stack.append(n)
            else:
                stack.append(-n)
            n-=1
            i+=1
        return sum(stack)