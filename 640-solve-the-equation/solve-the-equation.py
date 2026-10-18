class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        def parse(expr):
            coeff = 0
            const = 0
            i = 0
            sign = 1
            n = len(expr)
            while i < n:
                if expr[i] == '+':
                    sign = 1
                    i += 1
                elif expr[i] == '-':
                    sign = -1
                    i += 1
                start = i
                while i < n and expr[i].isdigit():
                    i += 1
                num = int(expr[start:i]) if start < i else 1
                if i < n and expr[i] == 'x':
                    coeff += sign * num
                    i += 1
                else:
                    const += sign * num
            return coeff, const
        a1, b1 = parse(left)
        a2, b2 = parse(right)
        a = a1 - a2
        b = b2 - b1
        if a == 0:
            return "Infinite solutions" if b == 0 else "No solution"
        return f"x={b // a}"