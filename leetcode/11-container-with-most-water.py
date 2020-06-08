class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        n = len(height)
        left = 0
        right = n - 1
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = max(area, h * w)
            
            if h == height[left]:
                left += 1
            else:
                right -= 1
            
        return area
