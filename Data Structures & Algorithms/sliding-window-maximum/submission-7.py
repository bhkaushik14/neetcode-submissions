class Solution:
    '''def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        result = []
        best = float("infinity") * -1
        for i in range(0, k):
            if nums[i] > best:
                best = nums[i]
        for r in range(k - 1, len(nums)):
            l = r - k + 1
            if nums[r] > best and nums[r] > nums[l]:
                best = nums[r]
            l += 1
            
            result.append(best)
            if l > 0:
                best = max(nums[l:r + 1])
        
        return result'''

    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        q = collections.deque()
        l = r = 0
        result = []
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                result.append(nums[q[0]])
                l += 1
            r += 1
        
        return result
    