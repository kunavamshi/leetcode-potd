class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        common = float('inf') # Initialize with positive infinity
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                common = min(common, nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return common if common != float('inf') else -1