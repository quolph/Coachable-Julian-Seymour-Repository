from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue, new_queue, answer = deque([root]), deque(), []
        while queue:
            level = []
            while queue:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue, new_queue = new_queue, queue
            answer.append(level)
        return answer
