from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the occurrences of each element in nums1
        counts = Counter(nums1)
        
        # This will store the intersection result
        result = []
        
        # Iterate through nums2 and find common elements
        for num in nums2:
            if counts[num] > 0:  # If the element is present in nums1
                result.append(num)
                counts[num] -= 1  # Decrease the count of the element
        
        return result