class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        m = max(0, m)
        n = min(len(nums2), 200)
        length = min(200, m+n)
        if len(nums1) == m+n:
            nums1[m:] = nums2
            nums1.sort()