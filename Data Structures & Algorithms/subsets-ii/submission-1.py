class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        nums.sort()

        self.recurse([], nums, 0)

        return self.results

    def recurse(self, arr, nums, idx):
        if len(arr) <= len(nums) and idx < len(nums):
            self.recurse(arr + [nums[idx]], nums, idx + 1)
            val = nums[idx]
            while idx < len(nums) and nums[idx] == val:
                idx += 1
            self.recurse(arr, nums, idx)
        else:
            self.results.append(arr)