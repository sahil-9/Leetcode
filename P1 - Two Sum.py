#Question link - https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
	   '''Add values to a dictionary instead of using multiple for loops. This way efficiency can be handled.
'''
        nums_dict = {}
        for i, val in enumerate(nums):
            if (target - val) in nums_dict:
                return [nums_dict.get(target-val), i]
            nums_dict[val] = i