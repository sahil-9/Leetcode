#Quetion link - https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows>=len(s): return s
        res = [''] * numRows        # makes a list ["", "", ""]
        currRow = 0
        
        for char in s:
            res[currRow] += char
            if currRow == 0:
                step = 1
            elif currRow == (numRows - 1):
                step = -1
            currRow += step
        return ''.join(res)

	#'res' after each pass
        '''['P', '', '']
            ['P', 'A', '']
            ['P', 'A', 'Y']
            ['P', 'AP', 'Y']
            ['PA', 'AP', 'Y']
            ['PA', 'APL', 'Y']
            ['PA', 'APL', 'YI']
            ['PA', 'APLS', 'YI']
            ['PAH', 'APLS', 'YI']
            ['PAH', 'APLSI', 'YI']'''