class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = l = 0;
        length = math.inf;
        current_sum = 0

        while r < len(nums):
            current_sum += nums[r]
            while current_sum >= target:
                current_sum -= nums[l]
                length = r - l + 1 if r - l + 1 < length else length
                l += 1
            r += 1

        if length == math.inf:
            return 0
        return length
