# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        previous_level, end, level = 0, head, 0
        current = end
        start = None
        start_end = start
        start_end_pointer = head
        while True:
            level += 1
            if level > previous_level + n:
                if start_end is not None:
                    start_end.next = ListNode(val=start_end_pointer.val)
                    start_end = start_end.next
                else:
                    start = ListNode(val=head.val)
                    start_end = start
                start_end_pointer  = start_end_pointer.next
            if level >= previous_level + n:
                previous_level = level - n
                current = current.next
            if end.next is None:
                break
            else:
                end = end.next
        if start_end is not None:
            start_end.next = current
            return start
        if current is not None:
            return current
