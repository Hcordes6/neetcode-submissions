class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        pt1 = 0
        pt2 = len(heights) - 1
        mostArea = min(heights[pt1], heights[pt2]) * pt2
        
        while pt1 < pt2:
            currDist = pt2 - pt1
            currArea = min(heights[pt1], heights[pt2]) * currDist
            
            if mostArea < currArea:
                mostArea = currArea
            
            if heights[pt1] < heights[pt2]:
                pt1 += 1
            elif heights[pt1] > heights[pt2]:
                pt2 -= 1
            else:
                pt1 += 1
        
        return mostArea
