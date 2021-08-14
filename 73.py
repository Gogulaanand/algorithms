https://leetcode.com/explore/item/3888

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeros.append((i,j))
        
        for x,y in zeros:
            matrix[x] = [0 for i in range(len(matrix[x]))]
            for i in range(len(matrix)):
                matrix[i][y] = 0
        
                
            