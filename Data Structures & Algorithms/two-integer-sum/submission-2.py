class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index = 1
        for i in range(len(nums)):
            while index < len(nums):
                if nums[i] + nums[index] == target and index != i:
                    return [i, index]
                index += 1
            index = 0
        return []
        