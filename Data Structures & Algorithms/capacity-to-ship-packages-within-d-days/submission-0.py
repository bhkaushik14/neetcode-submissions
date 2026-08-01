class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        save = 0

        while l <= r:
            mid = (l + r) // 2
            curr_capacity = 0
            days_needed = 1

            for weight in weights:
                if curr_capacity + weight > mid:
                    days_needed += 1
                    curr_capacity = weight
                else:
                    curr_capacity += weight

            if days_needed > days:
                l = mid + 1
            else:
                r = mid - 1
                save = mid
        return save