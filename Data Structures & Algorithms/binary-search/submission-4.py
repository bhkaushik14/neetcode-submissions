class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        half = len(nums) // 2

        if nums[half] < target:
            result= self.search(nums[half + 1:], target)
            if result == -1:
                return -1
            
            return half + 1 + result

        elif nums[half] > target:
            return self.search(nums[:half], target)
        elif nums[half] == target:
            return half
            
