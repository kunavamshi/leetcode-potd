class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        i = 0
        j = n - 1
        p = n - 1

        while i <= j:
            if abs(nums[i]) > nums[j]:
                ans[p] = nums[i] * nums[i]
                p -= 1
                i += 1
            else:
                ans[p] = nums[j] * nums[j]
                p -= 1
                j -= 1

        return ans