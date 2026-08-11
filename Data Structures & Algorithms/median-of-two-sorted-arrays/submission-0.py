class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        
        l, r = 0, len(nums1) - 1

        mid = (l + r) // 2

        return nums1[mid] if len(nums1) % 2 == 1 else (nums1[mid] + nums1[mid + 1]) / 2