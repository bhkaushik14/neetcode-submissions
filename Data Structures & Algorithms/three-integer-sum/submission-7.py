class Solution:
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        hold = []

        index = 0
        while index < len(nums):
            for i in range(index+1, len(nums)):
                curr = nums[index] + nums[i]
                for j in range(i + 1, len(nums)):
                    curr_l = sorted([nums[index], nums[i], nums[j]])
                    if curr + nums[j] == 0 and curr_l not in hold:
                        hold.append(curr_l)
            index += 1
        return hold
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        t3sum = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums) - 1
            num = nums[i]

            if nums[i] > 0:
                break

            while left < right:
                total = num + nums[left] + nums[right]
                if total == 0:
                    t3sum.append([num, nums[left], nums[right]])

                    left_val, right_val = nums[left], nums[right]
                    left += 1
                    right -= 1

                    while nums[left] == left_val and left < right:
                        left += 1

                    while nums[right] == right_val and right > left:
                        right -= 1 
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return t3sum

