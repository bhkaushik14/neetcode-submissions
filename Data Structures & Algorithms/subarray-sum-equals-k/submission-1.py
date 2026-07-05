class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0

        sums = {0: 1} 
        
        for num in nums:
            current_sum += num
            if (current_sum - k) in sums:
                count += sums[current_sum - k]
                
            sums[current_sum] = sums.get(current_sum, 0) + 1
            
        return count
