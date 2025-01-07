class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node, parent_depth):
            left_depth = right_depth = 0
            if node.left:
                left_subtree, left_depth = helper(node.left, parent_depth + 1)
            if node.right:
                right_subtree, right_depth = helper(node.right, parent_depth + 1)
            if left_depth == right_depth:
                if left_depth == 0:
                    return (node, parent_depth + 1)
                return (node, left_depth)
            elif left_depth > right_depth:
                return (left_subtree, left_depth)
            return (right_subtree, right_depth)
        subtree, max_depth = helper(root, 0)
        return subtree
