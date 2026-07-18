import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        
        # Turn the initial numbers into a min-heap
        heapq.heapify(self.heap)
        
        # If the initial array is larger than k, pop the smallest 
        # elements until we only have the k largest left
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Push the new value into the stream
        heapq.heappush(self.heap, val)
        
        # If our heap exceeds size k, pop the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # The root is always the k-th largest element
        return self.heap[0]