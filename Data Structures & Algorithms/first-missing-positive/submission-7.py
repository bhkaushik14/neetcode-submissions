class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1

        setNums = set(nums)

        index = 1
        while index <= len(nums) + 1:
            if index not in setNums:
                return index
            index += 1
        
            