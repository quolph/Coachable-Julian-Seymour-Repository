class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def revalidate(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            if node.left:
                validate(node.left, None, None)
            if node.right:
                validate(node.right, None, None)
            return -1
        def validate(node: Optional[TreeNode], x: Optional[TreeNode], y: Optional[TreeNode]) -> int:
            if not node:
                return -1
            if x and node.val <= x.val:
                return revalidate(node)
            if y and node.val >= y.val:
                return revalidate(node)
            if node.left:
                left = validate(node.left, x, node)
                if node.left.val >= node.val or left == -1:
                    return revalidate(node)
            else:
                left = 0
            if node.right:
                right = validate(node.right, node, y)
                if node.right.val <= node.val or right == -1:
                    return revalidate(node)
            else:
                right = 0
            ans = 1 + left + right
            self.answer = max(self.answer, ans)
            return ans
        validate(root, None, None)
        return self.answer
