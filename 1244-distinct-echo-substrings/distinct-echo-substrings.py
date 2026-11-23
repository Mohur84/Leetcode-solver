class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        base = 31
        mod1 = 10**9 + 7
        mod2 = 10**9 + 9
        prefix1 = [0] * (n + 1)
        prefix2 = [0] * (n + 1)
        power1 = [1] * (n + 1)
        power2 = [1] * (n + 1)
        for i in range(n):
            value = ord(text[i])
            prefix1[i + 1] = (prefix1[i] * base + value) % mod1
            prefix2[i + 1] = (prefix2[i] * base + value) % mod2
            power1[i + 1] = (power1[i] * base) % mod1
            power2[i + 1] = (power2[i] * base) % mod2
        def get_hash(prefix, power, mod, start, length):
            return (
                prefix[start + length]
                - prefix[start] * power[length]
            ) % mod
        seen = set()
        for length in range(1, n // 2 + 1):
            for i in range(n - 2 * length + 1):
                h1 = get_hash(prefix1, power1, mod1, i, length)
                h2 = get_hash(prefix1, power1, mod1, i + length, length)
                h3 = get_hash(prefix2, power2, mod2, i, length)
                h4 = get_hash(prefix2, power2, mod2, i + length, length)
                if h1 == h2 and h3 == h4:
                    seen.add((length, h1, h3))
        return len(seen)