class Solution:
    def maxFrequencyElements(self, nums):
        freq = {}
        max_freq = 0
        
        # Count frequencies of elements
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            max_freq = max(max_freq, freq[num])
        
        # Count elements with maximum frequency
        count_max_freq = sum(1 for num, f in freq.items() if f == max_freq)
        
        return count_max_freq * max_freq

# Example usage:
if __name__ == "__main__":
    nums = [1, 2, 2, 3, 1, 4]
    ob = Solution()
    print(ob.maxFrequencyElements(nums))  # Output: 4