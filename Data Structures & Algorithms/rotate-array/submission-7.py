class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hold = []

        new = nums.copy()

        norm_k = (k % len(nums))
        split = len(nums) - norm_k

        if norm_k != 0:
            for i in range(split):
                nums[i+norm_k] = new[i]
            
            for i in range(split, len(nums)):
                hold.append(new[i])
            
            nums[:norm_k] = hold

        
         