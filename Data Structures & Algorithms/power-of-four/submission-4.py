class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n % 4 != 0:
            if n == 1:
                return True
            return False
        for i in range(0, n):
            if 4**i == n:
                return True
            if 4 ** i > n:
                return False
        
        return False