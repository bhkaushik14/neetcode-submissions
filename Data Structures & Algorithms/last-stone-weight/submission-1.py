import heapq
# push
# pop
# heapq.heappush(stones, x)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for num in stones:
            heapq.heappush(max_heap, -num)

        while len(max_heap) > 1:
            print(max_heap)
            # x = max_heap.pop() * -1
            # y = max_heap.pop() * -1
            x = heapq.heappop(max_heap) * -1
            y = heapq.heappop(max_heap) * -1

            print(max_heap)
            if x < y:
                y = y - x
                heapq.heappush(max_heap, -y)
            elif x > y:
                x = x - y
                heapq.heappush(max_heap, -x)


        if len(max_heap) == 0:
            return 0
        return max_heap[0] * -1

            



