from typing import Optional

class ListNode:
    def __init__(self, val: int, necst=None):
        self.val = val
        self.next = necst

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        tail = dummy = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            v3 = v1 + v2 + carry
            carry = v3//10
            tail.next = ListNode(v3 % 10)
            tail = tail.next
        return dummy.next
