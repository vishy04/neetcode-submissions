import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean_heap = []

        for coordinate in points:
            euclidean_distance = math.sqrt((coordinate[0])**2 + (coordinate[1])**2)
            heapq.heappush(euclidean_heap , (-euclidean_distance,coordinate)) 
        
        while len(euclidean_heap) > k:
            heapq.heappop(euclidean_heap)
        
        return list(euclidean[1] for euclidean in euclidean_heap)
