class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        transitions=defaultdict(list)
        for triple in allowed:
            transitions[triple[:2]].append(triple[2])
        @lru_cache(None)
        def can_build(row:str)->bool:
            if len(row)==1:
                return True
            next_row=[]
            def backtrack(i:int)->bool:
                if i==len(row)-1:
                    return can_build("".join(next_row))
                pair=row[i:i+2]
                for block in transitions[pair]:
                    next_row.append(block)
                    if backtrack(i+1):
                        return True
                    next_row.pop()
                return False
            return backtrack(0)
        return can_build(bottom)