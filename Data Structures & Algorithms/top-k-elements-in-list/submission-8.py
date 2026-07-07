class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        sorted_items = sorted(hashMap.items(), key=lambda item: item[1], reverse=True)

        output = []
        for i in range(k):
            output.append(sorted_items[i][0])

        return output
        
        