class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        for num in nums:
            majority[num] = majority.get(num, 0) + 1
        
        print(majority)
        return max(majority, key = majority.get)