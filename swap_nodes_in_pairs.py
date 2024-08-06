# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if current is None:
            return None
        ans = current.next
        if ans is None:
            return head
        end = current
        while True:
            if current is None:
                break
            next_element = current.next
            if next_element is None:
                break
            end.next = next_element
            end = current
            tail = next_element.next
            current.next = tail
            next_element.next = current
            current = tail
            if current is None:
                break
        return ans
