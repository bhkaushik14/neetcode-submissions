import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for point in points:
            dist.append((math.sqrt(point[0]**2 + point[1]**2), point))

        h = dist
        heapq.heapify(h)
        results = []

        while k > 0:
            d, point = heapq.heappop(h)
            results.append(point)
            k -= 1
        
        return results

