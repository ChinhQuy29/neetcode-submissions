class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        area = min(heights[left], heights[right]) * (right - left)
        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            new_area = min(heights[left], heights[right]) * (right - left)
            area = max(area, new_area)
        return area