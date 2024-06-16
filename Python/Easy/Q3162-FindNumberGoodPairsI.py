class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt = 0
        n, m = len(nums1), len(nums2)

        for i in range(n):
            for j in range(m):
                if nums1[i] % (nums2[j] * k) == 0:
                    cnt += 1
        return cnt
