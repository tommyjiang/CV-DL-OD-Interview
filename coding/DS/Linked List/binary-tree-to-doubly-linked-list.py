class Solution:
    def bst-to-doubly-linked-list(self, root: TreeNode) -> TreeNode:
        self.last = None

        def dfs(node):
            if not node:
                return

            dfs(root.left)

            root.left = self.last

            if self.last:
                self.last.right = node

            self.last = node

            dfs(root.right)

        dfs(root)

        while root.left:
            root = root.left

        return root
