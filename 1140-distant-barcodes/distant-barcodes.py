class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        freq=Counter(barcodes)
        heap=[(-count, num) for num, count in freq.items()]
        heapq.heapify(heap)
        result=[]
        while len(heap)>=2:
            count1, num1=heapq.heappop(heap)
            count2, num2=heapq.heappop(heap)
            result.extend([num1, num2])
            count1+=1
            count2+=1
            if count1<0:
                heapq.heappush(heap, (count1, num1))
            if count2<0:
                heapq.heappush(heap, (count2, num2))
        if heap:
            result.append(heap[0][1])
        return result