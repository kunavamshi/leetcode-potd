from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number in the array
        freq = Counter(nums)
        
        # Sort the array based on frequency first (increasing), and by value second (decreasing)
        nums.sort(key=lambda x: (freq[x], -x))
        
        return nums