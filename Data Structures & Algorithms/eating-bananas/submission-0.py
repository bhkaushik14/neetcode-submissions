class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
            
        if total < h:
            return 1
        
        l, r = 1, max(piles)
        save = 0
        while l <= r:
            mid = (l + r) // 2
            curr_h = sum(pile // mid + (1 if pile % mid != 0 else 0) for pile in piles)
            if curr_h > h:
                l = mid + 1
            elif curr_h <= h:
                save = mid
                r = mid - 1
        return save