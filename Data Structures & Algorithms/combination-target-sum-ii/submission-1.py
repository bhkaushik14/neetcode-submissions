import bisect
class Solution:
    # Pick a number, then from that number, diverge
    # First choice: Pick the number
    # Then, again, choose to pick the number, always checking if its <= target or not.
    # if its > target, let go
    # Second choice:
    # dont pick the number, then pick the next number (or dont), and go all the way through till sum is target

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        candidates.sort()


        self.recurse([], candidates, target, 0, 0)

        unique_l1 = [list(t) for t in dict.fromkeys(tuple(x) for x in self.results)]

        return unique_l1
    
    def recurse(self, arr, nums, target, total, idx):
        # base case, if total, then add to results
        if total == target:
            self.results.append(arr)
        # check to see if its still under target, and if so, first add number
        # second choice skips number
        elif total < target and idx != len(nums):
            self.recurse(arr + [nums[idx]], nums, target, total + nums[idx], idx + 1)
            val = nums[idx]
            while idx < len(nums) and nums[idx] == val:
                idx += 1
            self.recurse(arr, nums, target, total, idx)
        
    
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        self.total_count = {}
        for num in candidates:
            self.total_count[num] = self.total_count.get(num, 0) + 1

        self.recurse([], candidates, 0, target, 0)

        return self.results

    def recurse(self, arr, nums, start, target, total):
        curr_count = {}

        if total == target:
            self.results.append(arr)
        elif total < target:
            for i in range(start, len(nums)):
                curr_count[nums[i]] = curr_count.get(nums[i], 0) + 1
                if curr_count[nums[i]] <= self.total_count[nums[i]]:
                    self.recurse(arr + [nums[i]], nums, i + 1, target, total + nums[i])
    '''

