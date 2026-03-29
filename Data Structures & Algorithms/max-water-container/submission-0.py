class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
    
        for l in range(0,len(heights)-1):
            r= len(heights)-1
            while(l<r):
                max_hei = min(heights[l],heights[r])*(r-l)

                if max_hei > max:
                    max = max_hei
                else:
                    r -=1
        return max        
            