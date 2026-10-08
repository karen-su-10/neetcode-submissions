class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        pl,pr = 0, len(heights)-1
        while pl<pr:
            current_amount = (pr-pl)*min(heights[pl], heights[pr])
            max_amount = max(max_amount, current_amount)
            if heights[pl] < heights[pr]:
                pl +=1
            else:
                pr -=1
        return max_amount
        