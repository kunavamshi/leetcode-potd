class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Create a dictionary to store the indices of characters in order
        order_indices = {char: i for i, char in enumerate(order)}
        
        # Define a custom sorting key function
        def custom_key(char):
            # If the character is in order, return its index
            # Otherwise, return a high value so it will be sorted after the characters in order
            return order_indices.get(char, float('inf'))
        
        # Sort the characters of s based on the custom sorting key
        sorted_s = sorted(s, key=custom_key)
        
        # Join the sorted characters to form the final string
        return ''.join(sorted_s)

# Example usage:
order1 = "cba"
s1 = "abcd"
order2 = "bcafg"
s2 = "abcd"
ob = Solution()
print(ob.customSortString(order1, s1))  # Output: "cbad"
print(ob.customSortString(order2, s2))  # Output: "bcad"