import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.size = len(nums)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.size += 1
        idx = self.size - self.k
        # while idx >= 0:
        #     print(self.heap)
        #     num = heapq.heappop(self.heap)
        #     if idx == 0:
        #         return num
            # idx -= 1
        while (len(self.heap) > self.k):
            heapq.heappop(self.heap)
        return self.heap[0]