class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        count = nums.count(0)

        for i in range(count):
            nums.remove(0)
            nums.append(0)