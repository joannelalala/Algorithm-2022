from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary, aka a map in other languages, to store the (inx, value) pairs of the iterations
        d = {}

        for idx, val in enumerate(nums): # utilize "enumrate" to get (key, value) pairs
            m = target - val # the difference between the target and the current value
            # now we are going to see if m exists in the dictionary, if it does, we get the paired indices; if not, we add the index to the dictionary
            if m in d:
                return [d[m], idx]
            else:
                d[val] = idx

# https://leetcode.com/problems/two-sum/



