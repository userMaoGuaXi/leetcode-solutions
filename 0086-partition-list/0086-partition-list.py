# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_dummy, large_dummy = ListNode(), ListNode()
        small_tail, large_tail = small_dummy, large_dummy

        cur = head
        while cur:
            nxt = cur.next
            cur.next = None

            if cur.val < x:
                small_tail.next = cur
                small_tail = small_tail.next
            else:
                large_tail.next = cur
                large_tail = large_tail.next
            cur = nxt
        
        small_tail.next = large_dummy.next
        return small_dummy.next

