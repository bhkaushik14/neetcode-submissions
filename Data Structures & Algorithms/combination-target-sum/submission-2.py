class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.results = []

        self.recurse([], nums, target, 0, 0)

        return self.results

    def recurse(self, arr, nums, target, curr_sum, start):
        if curr_sum == target:
            self.results.append(arr)
        elif curr_sum < target:
            for i in range(start, len(nums)):
                self.recurse(arr + [nums[i]], nums, target, curr_sum + nums[i], i)