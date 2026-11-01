import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = points
        heapq.heapify(h)
        results = []

        # while k > 0:
        #     point = heapq.heappop(h)
        #     dist = math.sqrt(point[0]**2 + point[1]**2)
        #     results.append(point)
        #     k -= 1
        
        # return results

        for i in range(len(points)):
            point = heapq.heappop(h)
            dist = math.sqrt(point[0]**2 + point[1]**2)
            results.append((dist, point))
        
        h2 = results
        heapq.heapify(h2)
        results = []

        while k > 0:
            dist, point = heapq.heappop(h2)
            results.append(point)
            k -= 1
        
        return results

