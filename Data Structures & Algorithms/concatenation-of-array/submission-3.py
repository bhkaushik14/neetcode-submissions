class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        i = 0
        j = n - 1
        k = (2 * n) - 1

        while (i < k) :
            ans[i] = nums[i]
            ans[k] = nums[j]

            i += 1
            k -= 1
            j -= 1
        return ans
        