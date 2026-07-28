class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0

        tallest_left = 0
        tallest_right = 0

        while left < right:
            if height[left] > tallest_left:
                tallest_left = height[left]
            if height[right] > tallest_right:
                tallest_right = height[right]

            max_height = min(tallest_left,tallest_right)
            
            if tallest_left < tallest_right:
                area += max_height - height[left]
                left += 1
            elif tallest_right < tallest_left:
                area += max_height - height[right]
                right -= 1
            else:
                area += max_height - height[left]
                left += 1

        return area
