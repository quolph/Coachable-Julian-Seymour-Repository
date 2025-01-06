class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue, next_queue = collections.deque([root]), collections.deque()
        end = False
        while queue:
            while queue:
                node = queue.popleft()
                if end and (node.left or node.right):
                    return False
                elif node.left:
                    next_queue.append(node.left)
                elif node.right:
                    return False
                if node.right:
                    next_queue.append(node.right)
                elif not (node.left and node.right):
                    end = True
            queue, next_queue = next_queue, queue
        return True
