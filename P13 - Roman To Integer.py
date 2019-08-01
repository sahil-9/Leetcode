#Question Link - https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        #Create a dictionary of values
	   val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = val[s[0]]
        for i in range(1, len(s)):
            if val[s[i]] > val[s[i-1]]:
                res -= val[s[i-1]] * 2		#if the next value is #greater than subtract the previous value twice since added #earlier
            res += val[s[i]]
        return res