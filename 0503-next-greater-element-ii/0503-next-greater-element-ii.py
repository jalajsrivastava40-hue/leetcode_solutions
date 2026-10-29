class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        st = []
        for i in range(len(nums)):
            ans = -1
            for j in range(1, len(nums)):
                idx = (i+j)%len(nums)
                if nums[idx] > nums[i]:
                    ans = nums[idx]
                    break
            st.append(ans)
        return st