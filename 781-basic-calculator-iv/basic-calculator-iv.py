class Solution:
    def basicCalculatorIV(
        self,
        expression: str,
        evalvars: List[str],
        evalints: List[int]
    ) -> List[str]:
        values = dict(zip(evalvars, evalints))
        def make_term(coef, vars=()):
            return {tuple(sorted(vars)): coef} if coef else {}
        def add(a, b, sign=1):
            result = defaultdict(int)
            for term, coef in a.items():
                result[term] += coef
            for term, coef in b.items():
                result[term] += sign * coef
            return {term: coef for term, coef in result.items() if coef}
        def multiply(a, b):
            result = defaultdict(int)
            for term1, coef1 in a.items():
                for term2, coef2 in b.items():
                    term = tuple(sorted(term1 + term2))
                    result[term] += coef1 * coef2
            return {term: coef for term, coef in result.items() if coef}
        tokens = []
        i = 0
        while i < len(expression):
            ch = expression[i]
            if ch == ' ':
                i += 1
            elif ch in '+-*()':
                tokens.append(ch)
                i += 1
            else:
                j = i
                while j < len(expression) and expression[j].isalnum():
                    j += 1
                tokens.append(expression[i:j])
                i = j
        def parse(pos):
            stack = []
            op = '+'
            while pos < len(tokens):
                token = tokens[pos]
                if token == ')':
                    break
                if token == '(':
                    value, pos = parse(pos + 1)
                elif token in '+-*':
                    op = token
                    pos += 1
                    continue
                else:
                    pos += 1
                    if token.isdigit():
                        value = make_term(int(token))
                    elif token in values:
                        value = make_term(values[token])
                    else:
                        value = make_term(1, (token,))
                if op == '*':
                    stack[-1] = multiply(stack[-1], value)
                else:
                    stack.append(value)
                if op == '-':
                    stack[-1] = {
                        term: -coef for term, coef in stack[-1].items()
                    }
                    op = '+'
            result = {}
            for item in stack:
                result = add(result, item)
            return result, pos + 1
        polynomial, _ = parse(0)
        terms = sorted(
            polynomial.items(),
            key=lambda item: (-len(item[0]), item[0])
        )
        answer = []
        for variables, coef in terms:
            monomial = "*".join(variables)
            answer.append(str(coef) + ("*" + monomial if monomial else ""))
        return answer