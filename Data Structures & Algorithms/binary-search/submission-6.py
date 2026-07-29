class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            h = l + ((r - l) // 2)
            if nums[h] >= target:
                r = h
            elif nums[h] < target:
                l = h + 1
        return l if (l < len(nums) and nums[l] == target) else -1