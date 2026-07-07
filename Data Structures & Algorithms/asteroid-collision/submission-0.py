class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            survive = True
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue

                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    survive = False
                    break

                else:
                    survive = False
                    break
            if survive:
                stack.append(asteroid)

        return stack