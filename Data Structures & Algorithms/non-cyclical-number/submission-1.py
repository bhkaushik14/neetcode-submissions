class Solution:
    def isHappy(self, n: int) -> bool:
        s1 = set()

        while True:
            n = sum([int(num) ** 2 for num in str(abs(n))])
            if n == 1:
                return True
            elif n in s1:
                return False 
            s1.add(n)
            
        
    
