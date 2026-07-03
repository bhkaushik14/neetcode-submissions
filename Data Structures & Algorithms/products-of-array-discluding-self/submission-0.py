class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        dict1 = defaultdict(list)

        for i in range(len(nums)):
            dict1[i] = nums[:i] + nums[i + 1:]
        
        for i in range(len(nums)):
            dict1[i] = math.prod(dict1[i])

        return list(dict1.values())