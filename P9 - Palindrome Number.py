#Question Link - https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        if x < 10:
            return True
        if (x % 10 == 0):
                return False
        temp = x
        num = 0
        while(temp > 0):
            digit = temp % 10
            num = digit + (num * 10)
            temp = temp // 10
        
        return num == x