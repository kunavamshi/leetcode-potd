from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log != "./":
                stack.append(log)
                
        return len(stack)

# Example usage:
solution = Solution()
print(solution.minOperations(["d1/","d2/","../","d21/","./"]))  # Output: 2
print(solution.minOperations(["d1/","d2/","./","d3/","../","d31/"]))  # Output: 3
print(solution.minOperations(["d1/","../","../","../"]))  # Output: 0