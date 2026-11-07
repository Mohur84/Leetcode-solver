class Solution:
    def smallestEquivalentString(self, s1, s2, baseStr):
        parent = list(range(26))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                if root_a < root_b:
                    parent[root_b] = root_a
                else:
                    parent[root_a] = root_b
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))
        result = []
        for ch in baseStr:
            root = find(ord(ch) - ord('a'))
            result.append(chr(root + ord('a')))
        return ''.join(result)