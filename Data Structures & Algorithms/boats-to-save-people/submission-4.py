class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()

        left, right = 0, len(people) - 1

        while left < right:
            count += 1

            if people[left] + people[right] <= limit:
                left += 1
            right -= 1

        if right - left == 0:
            return count + 1

        return count