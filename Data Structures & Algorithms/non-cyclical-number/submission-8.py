class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while True:
            slow = self.check(slow)
            fast = self.check(self.check(fast))

            if slow == fast:
                return slow == 1

    def check(self, n):
        return sum(int(num) ** 2 for num in str(n))