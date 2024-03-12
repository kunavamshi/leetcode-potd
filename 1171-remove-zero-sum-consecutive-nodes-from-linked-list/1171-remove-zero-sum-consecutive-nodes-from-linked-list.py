class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sum_map = {0: dummy}
        
        while head:
            prefix_sum += head.val
            if prefix_sum in prefix_sum_map:
                prev = prefix_sum_map[prefix_sum]
                start = prev.next
                curr_sum = prefix_sum
                while start != head:
                    curr_sum += start.val
                    prefix_sum_map.pop(curr_sum)
                    start = start.next
                prev.next = head.next
            else:
                prefix_sum_map[prefix_sum] = head
            head = head.next
        
        return dummy.next