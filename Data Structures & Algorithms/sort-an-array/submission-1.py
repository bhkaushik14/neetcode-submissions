class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # selection sort
        hold = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    hold = nums[i]
                    nums[i] = nums[j]
                    nums[j] = hold
        return nums