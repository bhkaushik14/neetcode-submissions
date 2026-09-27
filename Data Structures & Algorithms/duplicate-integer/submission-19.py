class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s1 = set()

        for num in nums:
            if num in s1:
                return True
            s1.add(num)
        
        return False
        