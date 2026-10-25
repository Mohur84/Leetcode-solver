from collections import defaultdict
from typing import List
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)
        for entry in cpdomains:
            count, domain = entry.split()
            count = int(count)
            parts = domain.split('.')
            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                counts[subdomain] += count
        return [
            f"{count} {domain}"
            for domain, count in counts.items()
        ]