class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-stone for stone in stones]
        #max heap
        heapq.heapify(heap)
        
        while len(heap) > 1:
            #heap[1] doesnt guarantee the second largest
            # if heap[0] == heap[1]:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            if stone1 != stone2: # w1 > w2 always(if not equal) as popped in heap
                heapq.heappush(heap, stone1 - stone2)
            #if equal default case
            
        
        return -heap[0] if heap else 0