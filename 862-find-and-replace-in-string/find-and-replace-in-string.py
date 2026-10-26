from typing import List
class Solution:
    def findReplaceString(
        self,
        s: str,
        indices: List[int],
        sources: List[str],
        targets: List[str]
    ) -> str:
        operations = sorted(
            zip(indices, sources, targets),
            reverse=True
        )
        for idx, source, target in operations:
            if s[idx:idx + len(source)] == source:
                s = s[:idx] + target + s[idx + len(source):]
        return s