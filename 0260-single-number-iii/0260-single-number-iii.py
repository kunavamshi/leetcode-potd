class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        # Step 1: XOR all the numbers to get the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a bit that is set in xor_all (this bit is different in the two unique numbers)
        # This bit will help us to divide the numbers into two groups
        # Here, we are finding the rightmost set bit
        rightmost_set_bit = xor_all & -xor_all
        
        # Step 3: Divide the numbers into two groups and XOR each group
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        # num1 and num2 are the two unique numbers
        return [num1, num2]