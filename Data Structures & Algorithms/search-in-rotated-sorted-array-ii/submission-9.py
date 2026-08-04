class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            print(f"MID: {mid}")
            print(f"Pre L: {l}")
            print(f"Pre R: {r}")
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[l] == nums[r]:
                l += 1
                r -= 1
                continue
            elif nums[mid] == nums[r]:
                r -= 1
            elif nums[mid] < nums[r]:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > target and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            print(f"Changed L: {l}")
            print(f"Changed R: {r}")
            
        return False