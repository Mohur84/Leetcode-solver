from collections import deque
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s):
            while True:
                i, n = 0, len(s)
                out = []
                changed = False
                while i < n:
                    j = i
                    while j < n and s[j] == s[i]:
                        j += 1
                    if j - i >= 3:
                        changed = True
                    else:
                        out.append(s[i:j])
                    i = j
                if not changed:
                    return s
                s = ''.join(out)
        hand = ''.join(sorted(hand))
        queue = deque([(board, hand, 0)])
        visited = {(board, hand)}
        while queue:
            b, h, steps = queue.popleft()
            for i in range(len(b) + 1):
                for j in range(len(h)):
                    if j > 0 and h[j] == h[j - 1]:
                        continue
                    if i > 0 and b[i - 1] == h[j]:
                        continue
                    extend_group = i < len(b) and b[i] == h[j]
                    split_pair = 0 < i < len(b) and b[i - 1] == b[i] and b[i] != h[j]
                    if not (extend_group or split_pair):
                        continue
                    new_board = clean(b[:i] + h[j] + b[i:])
                    new_hand = h[:j] + h[j + 1:]
                    if not new_board:
                        return steps + 1
                    if (new_board, new_hand) not in visited:
                        visited.add((new_board, new_hand))
                        queue.append((new_board, new_hand, steps + 1))
        return -1