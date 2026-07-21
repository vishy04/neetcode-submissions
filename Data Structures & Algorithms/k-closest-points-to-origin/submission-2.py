import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the k closest points to the origin (0, 0).
        
        Optimizations:
        1. Bounded Max-Heap: Pops elements mid-loop to keep the heap size at `k`. 
           This reduces time complexity to O(N log k) and space complexity to O(k).
        2. Squared Distance: Avoids computationally expensive math.sqrt() calls. 
           Comparing x^2 + y^2 yields the exact same sorting order as the true 
           Euclidean distance.
        """
        max_heap = []

        for x, y in points:
            # Calculate squared distance (no math.sqrt needed)
            dist_sq = (x**2) + (y**2)
            
            # Push negative distance to simulate a max-heap
            heapq.heappush(max_heap, (-dist_sq, [x, y])) 
            
            # Evict the furthest point immediately if we exceed k elements
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # Extract just the coordinates to return
        return [point for _, point in max_heap]