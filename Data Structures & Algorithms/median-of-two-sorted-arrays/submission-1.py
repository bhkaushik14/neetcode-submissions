class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        l, r = 0, len(a)

        mid = (len(a) + len(b) + 1) // 2
        while l <= r:
            i = (l + r) // 2
            j = mid - i

            a_left = a[i - 1] if i != 0 else -1 * math.inf
            a_right = a[i] if i != len(a) else math.inf

            b_left = b[j - 1] if j != 0 else -1 * math.inf
            b_right = b[j] if j != len(b) else math.inf                

            if a_left <= b_right and b_left <= a_right:
                lower = max(a_left, b_left)
                if (len(a) + len(b)) % 2 == 0:
                    higher = min(a_right, b_right)
                    return (lower + higher) / 2
                else:
                    return lower
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1 

            

"""
nums1 += nums2
        nums1.sort()
        
        l, r = 0, len(nums1) - 1

        mid = (l + r) // 2

        return nums1[mid] if len(nums1) % 2 == 1 else (nums1[mid] + nums1[mid + 1]) / 2
"""