class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        ans = 0
        for ch in sentences:
            a = len(ch.split())
            if a>ans:
                ans = a
        return ans 