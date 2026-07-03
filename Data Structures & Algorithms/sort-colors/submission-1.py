class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Selection sort
        hold = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] > nums[i]:
                    hold = nums[i]
                    nums[i] = nums[j]
                    nums[j] = hold

        print(nums)
        