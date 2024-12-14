from typing import List
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        answer = []
        queue, new_queue = deque(), deque()
        queue.append(root)
        while queue:
            level = []
            while queue:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            if len(answer) % 2 == 1:
                answer.append(level[::-1])
            else:
                answer.append(level)
            queue, new_queue = new_queue, queue
        return answer
