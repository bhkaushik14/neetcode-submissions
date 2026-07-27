class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        left, right = 0, len(heights) - 1

        while left < right:
            base = right - left
            height = min(heights[left], heights[right])
            if base * height > area:
                area = base * height
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1


        return area