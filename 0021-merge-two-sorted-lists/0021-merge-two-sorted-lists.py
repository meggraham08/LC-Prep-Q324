# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        tail = dummy
        curr_1 = list1
        curr_2 = list2
        
        # Merge process
        while curr_1 is not None and curr_2 is not None:
            if curr_1.val <= curr_2.val:
                tail.next = curr_1
                curr_1 = curr_1.next
            else:
                tail.next = curr_2
                curr_2 = curr_2.next
            
            # Move the tail pointer forward
            tail = tail.next

        # Append any remaining nodes from either list
        if curr_1 is not None:
            tail.next = curr_1
        if curr_2 is not None:
            tail.next = curr_2
        
        return dummy.next