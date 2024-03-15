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
        nums1[m:] = nums2
        nums1.sort()