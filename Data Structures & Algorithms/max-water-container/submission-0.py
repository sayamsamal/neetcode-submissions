class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxH = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                maxH = max(maxH, area)
        return maxH       