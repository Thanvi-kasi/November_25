# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Step 1: Get the length of the linked list
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        # Step 2: Reverse a segment of the linked list
        def reverse_linked_list(node, k):
            prev, curr = None, node
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Step 3: Main logic for reversing in k-groups
        length = get_length(head)
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while length >= k:
            group_start = group_prev.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next
            
            # Save the next group's start node
            next_group = group_end.next
            
            # Reverse the current k-group
            group_end.next = None
            group_prev.next = reverse_linked_list(group_start, k)
            
            # Connect the reversed group with the next group
            group_start.next = next_group
            
            # Move the group_prev pointer k steps ahead
            group_prev = group_start
            
            # Decrease length by k
            length -= k
        
        return dummy.next
