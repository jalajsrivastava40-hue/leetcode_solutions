class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def backtrack(i, curr_xor):
            if i == len(nums):
                return curr_xor
            take = backtrack(i+1, curr_xor^nums[i])
            skip = backtrack(i+1, curr_xor)
            return take+skip
        return backtrack(0,0)