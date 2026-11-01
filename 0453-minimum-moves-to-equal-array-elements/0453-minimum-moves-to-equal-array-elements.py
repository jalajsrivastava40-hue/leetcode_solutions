class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimum = min(nums)
        a = 0
        for num in nums:
            a += num - minimum
        return a