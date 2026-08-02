class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[l] < nums[mid] and nums[r] < nums[l]:
                l = mid + 1
            elif nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1

            print(f"MID: {mid}")
            print(f"L: {l}, R: {r}")
        
        return nums[l]