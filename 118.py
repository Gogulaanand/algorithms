https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]
        
        for i in range(1, numRows):
            x = list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))
            res.append(x)
            
        return res
        
        
        
#         res=[[1]]
            
#         for i in range(1, numRows):
#             arr = [1 for j in range(i+1)]
#             for k in range(1, i):
#                 arr[k] = res[i-1][k-1] + res[i-1][k]
#             res.append(arr)

#         return res

        