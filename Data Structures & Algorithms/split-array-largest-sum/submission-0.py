class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        save = 0

        while l <= r:
            mid = (l + r) // 2
            sub_arr_count = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num > mid:
                    current_sum = num
                    sub_arr_count += 1
                else:
                    current_sum += num
            
            if sub_arr_count > k:
                l = mid + 1
            else:
                save = mid
                r = mid - 1
        return save
        