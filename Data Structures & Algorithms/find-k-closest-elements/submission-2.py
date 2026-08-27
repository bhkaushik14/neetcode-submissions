class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr

        l, r = 0, len(arr) - 1
        while r - l + 1 > k:
            if abs(arr[r] - x) >= abs(arr[l] - x):
                r -= 1
            else:
                l += 1
        return arr[l:r + 1]