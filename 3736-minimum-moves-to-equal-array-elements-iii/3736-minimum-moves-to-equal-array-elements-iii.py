class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        target = max(nums)
        for i in nums:
            ans += target - i
        return ans