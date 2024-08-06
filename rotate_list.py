# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        last, length, current = None, 0, head
        while current is not None:
            length += 1
            last = current
            current = current.next
        if length == 0:
            return head
        move = k % length
        move_start = length - move
        fss, fse = head, None
        step, current = 0, head
        while step < move_start:
            print(step, move_start)
            if step == move_start - 1:
                fse = current
            current = current.next
            step += 1
        ans = fse.next
        if ans is None:
            return head
        fse.next = None
        last.next = fss
        return ans
