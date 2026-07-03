class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1 = set(nums)
        longest = 0

        seq = []
        for num in s1:
            if (num - 1) not in s1:
                cur_num = num
                cur_len = 1

                while cur_num + 1 in s1:
                    cur_num += 1
                    cur_len += 1
                
                if cur_len > longest:
                    longest = cur_len
        return longest

    
