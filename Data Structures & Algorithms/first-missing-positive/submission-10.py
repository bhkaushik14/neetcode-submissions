class Solution:
    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # Wrong Solution
        # O(n) Time Complexity
        # O(n) Auxiliary Space
        
        setNums = set(nums)

        index = 1
        while index <= len(nums) + 1:
            if index not in setNums:
                return index
            index += 1
    '''

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
        
        
            