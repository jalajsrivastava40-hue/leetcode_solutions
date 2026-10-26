class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for num in nums1:
            ans = -1
            for i in range(len(nums2)):
                if nums2[i] == num:
                    for j in range(i+1, len(nums2)):
                        if nums2[j] > num:
                            ans = nums2[j]
                            break
                    break
            res.append(ans)
        return res