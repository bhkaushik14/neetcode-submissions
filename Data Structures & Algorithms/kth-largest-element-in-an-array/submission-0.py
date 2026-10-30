import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)

        while k > 0:
            x = heapq.heappop(max_heap) * -1
            if k == 1:
                return x
            k -= 1
