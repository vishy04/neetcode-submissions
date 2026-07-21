import heapq
class KthLargest:
    #Revision ( Tue 21 July )
    def __init__(self, k: int, nums: List[int]):
        self.minHeap , self.k = nums , k

        #heapify full -> keep only top k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #push first then pushpop 
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
    
        return self.minHeap[0]
        
