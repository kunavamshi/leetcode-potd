class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        remove_indices = set()
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    remove_indices.add(i)
                else:
                    stack.pop()
        
        # Add remaining unmatched open parentheses indices to remove_indices
        remove_indices.update(stack)
        
        # Build the result string excluding characters at indices in remove_indices
        result = ""
        for i, char in enumerate(s):
            if i not in remove_indices:
                result += char
                
        return result