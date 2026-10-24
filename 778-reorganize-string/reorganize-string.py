class Solution:
    def reorganizeString(self, s: str) -> str:
        freq=Counter(s)
        n=len(s)
        if max(freq.values())>(n+1)//2:
            return ""
        heap=[(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)
        result=[]
        prev_count=0
        prev_char=""
        while heap:
            count, char=heapq.heappop(heap)
            result.append(char)
            if prev_count<0:
                heapq.heappush(heap, (prev_count, prev_char))
            prev_count=count+1
            prev_char=char
        return "".join(result)