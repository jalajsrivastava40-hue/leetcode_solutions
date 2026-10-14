class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            a = 0
            if num < 10:
                a = 1
                continue
            while num > 0:
                num //= 10
                a += 1
            if a%2 == 0:
                ans += 1
        return ans