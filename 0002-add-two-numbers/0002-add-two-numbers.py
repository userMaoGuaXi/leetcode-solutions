# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        p, q = l1, l2
        carry = 0

        while p or q or carry:
            x = p.val if p else 0
            y = q.val if q else 0
            s = x + y + carry

            carry, digit = divmod(s, 10)
            tail.next = ListNode(digit)
            tail = tail.next

            p = p.next if p else None
            q = q.next if q else None

        return dummy.next