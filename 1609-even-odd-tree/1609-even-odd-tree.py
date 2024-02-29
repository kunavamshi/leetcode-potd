from collections import deque
from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        queue = deque([(root, 0)])  # Initialize queue with root and its level index
        while queue:
            prev_val = None  # To track the previous value in the current level
            level_size = len(queue)
            for _ in range(level_size):
                node, level = queue.popleft()
                
                # Check if the current node's value violates the conditions
                if (level % 2 == 0 and (node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val))) or \
                   (level % 2 != 0 and (node.val % 2 != 0 or (prev_val is not None and node.val >= prev_val))):
                    return False
                
                prev_val = node.val  # Update prev_val for the next iteration
                
                # Add child nodes to the queue if they exist
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
                    
        return True