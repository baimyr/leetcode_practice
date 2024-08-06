# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a_pointer = l1
        b_pointer = l2
        origin = ListNode()
        answer_pointer = origin
        remainder = 0
        while True:
            a_val = a_pointer.val if a_pointer is not None else 0
            b_val = b_pointer.val if b_pointer is not None else 0

            sum_val = a_val + b_val + remainder
            if sum_val >= 10:
                remainder = 1
                sum_val = sum_val - 10
            else:
                remainder = 0
            answer_pointer.val = sum_val
            a_pointer = a_pointer.next if a_pointer is not None else None
            b_pointer = b_pointer.next if b_pointer is not None else None
            if a_pointer is None and b_pointer is None and remainder == 0:
                break
            answer_pointer.next = ListNode()
            answer_pointer = answer_pointer.next
        return origin
