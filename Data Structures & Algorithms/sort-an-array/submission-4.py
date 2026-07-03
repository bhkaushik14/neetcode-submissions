class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        # merge sort
        mid = len(nums) // 2
        leftL = self.sortArray(nums[:mid])
        rightL = self.sortArray(nums[mid:])

        return self.merge(leftL, rightL)

    def merge(self, leftL, rightL):
        sorted_arr = []
        i = j = 0

        while i < len(leftL) and j < len(rightL):
            if leftL[i] < rightL[j]:
                sorted_arr.append(leftL[i])
                i +=1 
            else:
                sorted_arr.append(rightL[j])
                j += 1
        
        sorted_arr.extend(leftL[i:])
        sorted_arr.extend(rightL[j:])
        
        print(sorted_arr)

        return sorted_arr
