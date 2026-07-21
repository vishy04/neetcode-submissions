import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Self Done Logic
        """
        euclidean_heap = []

        for coordinate in points:
            #avoiding sqrt as it is expensive ( we care about relative order not the value)
            euclidean_distance = (coordinate[0])**2 + (coordinate[1])**2

            heapq.heappush(euclidean_heap , (-euclidean_distance,coordinate)) 
            #pop if exceeds k
            if len(euclidean_heap) > k:
                heapq.heappop(euclidean_heap)
        
        #merge this loop inside in one single loop 
        # while len(euclidean_heap) > k:
        #     heapq.heappop(euclidean_heap)
        
        return list(euclidean[1] for euclidean in euclidean_heap)
