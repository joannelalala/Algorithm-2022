class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # The idea of the solution to this problem is to have a helper function
        # In the helper function, create a Counter to store the number of subarrays 
        # with the number of distinct elements exactly as 'k'
        return self.exactK(nums, k) - self.exactK(nums, k - 1)

    # create a helper function
    def exactK(self, nums, k):
        count = collections.Counter()
        res = i = 0

        for j in range(len(nums)):
            if count[nums[j]] == 0: # means the count of nums[j] is 0
                k -= 1
            count[nums[j]] += 1
            while k < 0:
                count[nums[i]] -= 1
                if count[nums[i]] == 0: # meaning the count of nums[i] is 0
                    k += 1
                i += 1
            res += j - i + 1
        return res

