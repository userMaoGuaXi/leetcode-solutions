# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head
        
        dummy = ListNode()
        dummy.next = head
        group_prev = dummy

        while True:
            kth = self._find_kth(group_prev, k)
            if not kth:
                break

            group_next = kth.next
            prev, curr = group_next, group_prev.next
            while curr is not group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            new_tail = group_prev.next
            group_prev.next = kth
            group_prev = new_tail
        
        return dummy.next

    def _find_kth(self, start: ListNode, k: int) -> Optional[ListNode]:
        """return kth node after `start`, or None if len < k"""
        cur = start
        for _ in range(k):
            cur = cur.next
            if cur is None:
                return None
        return cur


