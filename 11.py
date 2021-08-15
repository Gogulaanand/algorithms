https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        h = len(height)
# O(n)
        j = h-1
        i = 0
        while(i<j):
            area = min(height[j], height[i]) * (j-i)
            max_area = max(area, max_area)
            
            if height[j] < height[i]:
                j-=1
            else:
                i+=1
        
                
# O(n^2)
        # for i in range(h):
        #     for j in range(i+1, h):
        #         if height[i] > height[j]:
        #             area = height[j] * (j-i)    
        #         else:
        #             area = height[i] * (j-i)
        #         if area > max_area:
        #             max_area = area
        return max_area