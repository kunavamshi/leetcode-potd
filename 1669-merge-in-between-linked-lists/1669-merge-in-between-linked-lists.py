# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Iterate to the ath node
        current = list1
        for _ in range(a - 1):
            current = current.next
        
        # Connect the node before ath to the head of list2
        temp = current
        for _ in range(b - a + 2):
            temp = temp.next
        current.next = list2
        
        # Iterate to the end of list2
        while list2.next:
            list2 = list2.next
        
        # Connect the last node of list2 to the node after the bth node
        list2.next = temp
        
        return list1