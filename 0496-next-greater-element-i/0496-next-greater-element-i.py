class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        st = []
        nxt_grt = {}
        for num in nums2:
            while st and num > st[-1]:
                small = st.pop()
                nxt_grt[small] = num
            st.append(num)
        for num in st:
            nxt_grt[num] = -1
        ans = []
        for num in nums1:
            ans.append(nxt_grt[num])
        return ans