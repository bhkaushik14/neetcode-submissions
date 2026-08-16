class Solution:
    def isHappy(self, n: int) -> bool:
        # s1 = set()

        slow = n
        fast = n
        while True:
            if slow == 1:
                return True
    
            slow = self.check(slow)
            fast = self.check(self.check(fast))
            
            if slow == fast:
                break
        
        slow = n
        while slow != fast:
            slow = self.check(slow)
            fast = self.check(fast)

            if slow == 1:
                return True

        return False
        
    def check(self, n):
        return sum(int(num) ** 2 for num in str(n))
            
        
    
