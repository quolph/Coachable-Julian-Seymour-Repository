from collecitions import deque

class Node:
    def __init__(self, val: int = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next 
class Solution:
    def connect(self, root: Node) -> Node:
        node, head, prev = root, None, None
        while node:
            while node:
                if node.left:
                    if prev:
                        prev.next = node.left
                    else:
                        head = node.left
                    prev = node.left
                if node.right:
                    if prev:
                        prev.next = node.right
                    else:
                        head = node.right
                    prev = node.right
                node = node.next
            node, head, prev = head, None, None
        return root
    def connectCheating(self, root: Node) -> Node:
        if not root:
            return None
        queue, new_queue = deque([root]), deque()
        while queue:
            prev = None
            while queue:
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue, new_queue = new_queue, queue
        return root
