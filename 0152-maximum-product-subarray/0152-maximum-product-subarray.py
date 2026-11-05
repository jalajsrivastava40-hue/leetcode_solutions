class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            a = num * max_prod
            b = num * min_prod
            max_prod = max(num, a, b)
            min_prod = min(num, a, b)
            ans = max(ans, max_prod)
        return ans