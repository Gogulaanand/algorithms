https://leetcode.com/problems/excel-sheet-column-number

import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        store = (dict(zip(string.ascii_uppercase, range(1,27))))
        l = len(columnTitle)
        
        res = 0
        columnTitle = columnTitle[::-1]
        
        for i in range(l-1, -1, -1):
            res += store[columnTitle[i]]*pow(26, i)
        return res

        # for i, char in enumerate(reversed(columnTitle)):
        #     res += store[char]*pow(26, i)
        # return res