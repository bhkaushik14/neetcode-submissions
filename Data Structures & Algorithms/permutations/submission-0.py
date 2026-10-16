class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.recurse([], nums)

        return self.result
    
    def recurse(self, arr, nums):
        if len(arr) == len(nums):
            self.result.append(arr)
        elif len(arr) < len(nums):
            for num in nums:
                if num in arr:
                    continue
                
                self.recurse(arr + [num], nums)
        
