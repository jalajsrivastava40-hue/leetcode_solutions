class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            digit = str(num)
            max1 = max(digit)
            encrypted_val = int(max1*len(digit))
            ans += encrypted_val
        return ans