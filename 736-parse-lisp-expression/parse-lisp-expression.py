class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
            elif expression[i] in '()':
                tokens.append(expression[i])
                i += 1
            else:
                j = i
                while j < len(expression) and expression[j] not in ' ()':
                    j += 1
                tokens.append(expression[i:j])
                i = j
        def parse(pos, env):
            token = tokens[pos]
            if token != '(':
                if token.lstrip('-').isdigit():
                    return int(token), pos + 1
                return env[token], pos + 1
            op = tokens[pos + 1]
            pos += 2
            if op == 'add':
                a, pos = parse(pos, env)
                b, pos = parse(pos, env)
                return a + b, pos + 1
            if op == 'mult':
                a, pos = parse(pos, env)
                b, pos = parse(pos, env)
                return a * b, pos + 1
            local = env.copy()
            while True:
                token = tokens[pos]
                if token == '(' or token == ')':
                    value, pos = parse(pos, local)
                    return value, pos + 1
                if (
                    pos + 1 < len(tokens)
                    and tokens[pos + 1] == ')'
                ):
                    value, pos = parse(pos, local)
                    return value, pos + 1
                variable = token
                value, pos = parse(pos + 1, local)
                local[variable] = value
        result, _ = parse(0, {})
        return result