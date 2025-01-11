class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(node):
            if node.left:
                inorder(node.left)
            arr.append(node)
            if node.right:
                inorder(node.right)
            node.left = node.right = None
        def bst(nodes):
            n = len(nodes)
            if n == 0:
                return None
            elif n == 1:
                return nodes[0]
            mid = n//2
            node = nodes[mid]
            node.left = bst(nodes[:mid])
            node.right = bst(nodes[mid+1:])
            return node
        inorder(root)
        return bst(arr)
