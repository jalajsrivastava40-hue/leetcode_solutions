class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        a = nums[::-1]
        return a[k-1]