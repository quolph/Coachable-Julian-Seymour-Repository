from typing import Optional

class ListNode:
    def __init__(self, val=None, necst=None):
        self.val = val
        self.next = necst
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cursor = head = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                cursor.next = list1
                list1 = list1.next
            else:
                cursor.next = list2
                list2 = list2.next
            cursor = cursor.next
        if list1:
            cursor.next = list1
        if list2:
            cursor.next = list2
        return head.next
