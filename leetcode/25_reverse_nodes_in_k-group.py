from typing import Optional

class ListNode:
    def __init__(self, val: int, necst=None):
        self.val = val
        self.next = necst
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        for i in range(k):
            if not current:
                return head
            current = current.next
        previous = None
        current = head
        for i in range(k):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        head.next = self.reverseKGroup(current, k)
        return previous
    def reverseKGroupSlow(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next
        if len(nodes) < k:
            return head
        i = 0
        head = None
        tail = None
        current = None
        if len(nodes) == 1:
            while nodes:
                node = nodes.pop()
                if tail:
                    tail.next = node
                tail = node
            return node
        while i <= len(nodes):
            if i + k > len(nodes):
                break
            current = nodes[i]
            current.next = None
            for j in range(i+1, i+k):
                nodes[j].next = current
                current = nodes[j]
            if tail:
                tail.next = current
            if head is None:
                head = current
            tail = nodes[i]
            i += k
        if len(nodes) % k != 0:
            index = len(nodes) - len(nodes) % k
            tail.next = nodes[index]
        return head
