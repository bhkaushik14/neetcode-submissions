class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.recurseSubsets(nums, 0, [])

        return self.result
    def recurseSubsets(self, nums, idx, subset):
        if len(nums) == idx:
            copy = subset.copy()
            self.result.append(copy)
            return
        
        subset.append(nums[idx])
        self.recurseSubsets(nums, idx + 1, subset)
        subset.pop()
        self.recurseSubsets(nums, idx+1, subset)

        
        

# Take in [1,2,3]
# left: [1] i = 0
# right: [] i = 0
# both increment i by 1
# then for left -> left: take [1, 2]
# left -> right: take [1]
# right -> left: take [2]
# right -> right: take []...