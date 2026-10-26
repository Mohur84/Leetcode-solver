class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [('L', -1)]
        for i, ch in enumerate(dominoes):
            if ch != '.':
                symbols.append((ch, i))
        symbols.append(('R', len(dominoes)))
        result = list(dominoes)
        for j in range(1, len(symbols)):
            left_force, left_pos = symbols[j - 1]
            right_force, right_pos = symbols[j]
            if left_force == right_force:
                for i in range(left_pos + 1, right_pos):
                    result[i] = left_force
            elif left_force == 'R' and right_force == 'L':
                i, k = left_pos + 1, right_pos - 1
                while i < k:
                    result[i] = 'R'
                    result[k] = 'L'
                    i += 1
                    k -= 1
        return ''.join(result)