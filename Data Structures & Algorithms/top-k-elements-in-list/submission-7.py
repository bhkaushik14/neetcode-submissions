class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(list)

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1

        return sorted(dictionary, key=dictionary.get, reverse=True)[:k]


            