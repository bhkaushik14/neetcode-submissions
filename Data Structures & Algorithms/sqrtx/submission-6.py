class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        curr_best = 0

        while l <= r:
            mid = (l + r) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                curr_best = mid
                l = mid + 1
            else:
                r = mid - 1
        return curr_best