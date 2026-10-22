class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        result = []

        for num in arr:
            if num == 0:
                result.append(0)
                result.append(0)
            else:
                result.append(num)

        arr[:] = result[:len(arr)]