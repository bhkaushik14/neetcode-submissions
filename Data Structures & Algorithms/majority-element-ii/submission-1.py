class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        count = {}
        over3 = set()

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > (n/3):
                over3.add(num)
        
        return list(over3)