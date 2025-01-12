class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.found_p = self.found_q = False
        def dfs(node):
            if not node:
                return None
            left = dfs(node.left)
            right = dfs(node.right)
            if node == p:
                self.found_p = True
                return node
            elif node == q:
                self.found_q = True
                return node
            if left and right:
                return node
            return left or right
        answer = dfs(root)
        if self.found_p and self.found_q:
            return answer
        return None
    def lowestCommonAncestorSlow(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        root.depth = 0
        queue = deque([root])
        p.depth = q.depth = -1
        while queue:
            node = queue.popleft()
            if p.depth > -1 and q.depth > -1:
                queue = None
                break
            if node.left:
                node.left.parent = node
                node.left.depth = node.depth + 1
                queue.append(node.left)
            if node.right:
                node.right.parent = node
                node.right.depth = node.depth + 1
                queue.append(node.right)
        if p.depth == -1 or q.depth == -1:
            return None
        while p != q:
            if p.depth <= q.depth:
                if p.depth == q.depth:
                    p = p.parent
                q = q.parent
            elif p.depth > q.depth:
                p = p.parent
        return p
    def lowestCommonAncestorVerySlow(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque([(root, 0, [])])
        p_depth = q_depth = -1
        while queue:
            node, depth, path = queue.popleft()
            if node.val == p.val:
                p_depth = depth
                p_path = path
            elif node.val == q.val:
                q_depth = depth
                q_path = path
            if p_depth > -1 and q_depth > -1:
                queue = None
                break
            if node.left:
                queue.append((node.left, depth + 1, path + [node]))
            if node.right:
                queue.append((node.right, depth + 1, path + [node]))
        if p_depth == -1 or q_depth == -1:
            return None
        while p != q:
            if p_depth <= q_depth:
                if p_depth == q_depth:
                    p = p_path.pop()
                    p_depth -= 1
                q = q_path.pop()
                q_depth -= 1
            elif p_depth > q_depth:
                p = p_path.pop()
                p_depth -= 1
        return p
