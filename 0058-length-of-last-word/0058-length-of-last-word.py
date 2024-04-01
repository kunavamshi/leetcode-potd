class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading and trailing spaces
        s = s.strip()
        # Split the string by spaces
        words = s.split()
        # Return the length of the last word
        return len(words[-1])