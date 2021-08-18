https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]
        
        for i in range(1, numRows):
            x = list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))
            res.append(x)
            
        return res[-1]