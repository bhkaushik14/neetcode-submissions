class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s1 = set()

        for num in nums:
            if num in s1:
                return num
            s1.add(num)
        
        return -1