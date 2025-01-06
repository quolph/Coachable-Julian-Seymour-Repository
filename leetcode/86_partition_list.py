from typing import Optional

class ListNode:
    def __init__(self, val=0, necst=None):
        self.val = val
        self.next = necst
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = small_head = ListNode(0)
        big = big_head = ListNode(0)
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        small.next = big_head.next
        big.next = None
        return small_head.next
