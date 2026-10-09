class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        count = []
        def backtrack(i):
            if i == len(nums):
                ans.append(count.copy())
                return 
            count.append(nums[i])
            backtrack(i+1)
            count.pop()
            backtrack(i+1)
        backtrack(0)
        return ans