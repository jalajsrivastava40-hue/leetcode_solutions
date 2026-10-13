class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        ans1 = 0
        ans2 = 0
        for i in nums:
            if i > 0:
                ans1 += 1
            elif i < 0:
                ans2 += 1
        return max(ans1, ans2)