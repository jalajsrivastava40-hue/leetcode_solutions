class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        current = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            maxSum = max(maxSum, current)
        return maxSum