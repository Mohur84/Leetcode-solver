class Solution:
    def minMutation(self, startGene, endGene, bank):
        bank=set(bank)
        if endGene not in bank:
            return -1
        queue=deque([(startGene, 0)])
        visited={startGene}
        genes="ACGT"
        while queue:
            gene, steps=queue.popleft()
            if gene==endGene:
                return steps
            for i in range(8):
                for ch in genes:
                    if ch==gene[i]:
                        continue
                    next_gene=gene[:i]+ch+gene[i+1:]
                    if next_gene in bank and next_gene not in visited:
                        visited.add(next_gene)
                        queue.append((next_gene, steps+1))
        return -1