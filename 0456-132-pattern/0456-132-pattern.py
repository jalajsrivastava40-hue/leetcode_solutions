class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        st = []
        sec = float('-inf')
        for i in range(len(nums) -1, -1, -1):
            if nums[i] < sec:
                return True
            while st and nums[i] > st[-1]:
                sec = st.pop()
            st.append(nums[i])
        return False