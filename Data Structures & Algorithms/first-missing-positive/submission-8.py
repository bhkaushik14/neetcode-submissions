class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        setNums = set(nums)

        index = 1
        while index <= len(nums) + 1:
            if index not in setNums:
                return index
            index += 1
        
            