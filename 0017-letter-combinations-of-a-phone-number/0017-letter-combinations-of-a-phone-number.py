
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        count = []
        def backtrack(i):
            if i == len(digits):
                ans.append("".join(count))
                return
            letters = keypad[digits[i]]
            for letter in letters:
                count.append(letter)
                backtrack(i + 1)
                count.pop()
        backtrack(0)
        return ans