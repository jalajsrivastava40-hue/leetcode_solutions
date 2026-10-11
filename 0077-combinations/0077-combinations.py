class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        count = []
        def backtrack(start):
            if len(count) == k:
                ans.append(count.copy())
                return
            for i in range(start, n+1):
                count.append(i)
                backtrack(i+1)
                count.pop()
        backtrack(1)
        return ans