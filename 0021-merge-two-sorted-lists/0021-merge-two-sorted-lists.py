# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node needed
        dummy = ListNode(None)
        # set name of node and call it tail
        tail = dummy
        curr_1 = list1
        curr_2 = list2
        while curr_1 is not None and curr_2 is not None:
            if curr_1.val <= curr_2.val:
                tail.next = curr_1
                curr_1 = curr_1.next
            else:
                tail.next = curr_2
                curr_2 = curr_2.next
            tail = tail.next
        if curr_1 is not None:
            tail.next =  curr_1
        if curr_2 is not None:
            tail.next = curr_2
        # returning where to start, that is why we need to set tail = dummy for line 10
        return dummy.next