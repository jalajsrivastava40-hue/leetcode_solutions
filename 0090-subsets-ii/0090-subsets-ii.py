class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        count = []
        def backtrack(start):
            ans.append(count.copy())
            for i in range(start, len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                count.append(nums[i])
                backtrack(i+1)
                count.pop()
        backtrack(0)
        return ans