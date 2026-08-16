class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while True:
            if slow == 1:
                return True
    
            slow = self.check(slow)
            fast = self.check(self.check(fast))
            
            if slow == fast:
                if slow == 1:
                    return True
                else:
                    return False
        
    def check(self, n):
        return sum(int(num) ** 2 for num in str(n))
            
        
    
