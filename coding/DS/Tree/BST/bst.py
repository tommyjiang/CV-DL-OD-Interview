class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, root=None):
        self.root = None

    def search(self, val):
        node = self.root
        while node:
            if node.val == val:
                return True
            elif node.val < val:
                node = node.right
            elif node.val > val:
                node = node.left

        return False

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)

        node = self.root

        while node:
            if node.val == val:
                return False
            elif node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
            elif node.val > val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)

        return True

    def delete(self, val):
        found = self.search(val)
        if not found:
            print('No such node.')
            return False
        else:
            self._delete(val, self.root)
            return True

    def _delete(self, val, node):
        if not node:
            return None
        if node.val == val:
            if node.right:
                right_left_most = node.right
                while right_left_most.left:
                    right_left_most = right_left_most.left
                right_left_most.left = node.left
                return right_left_most
            else:
                return node.left
        elif node.val > val:
            node.left = self._delete(val, node.left)
        elif node.val < val:
            node.right = self._delete(val, node.right)

        return node

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)

    def print(self):
        self.inorder(self.root)

    def successor(self, val):
        node = self.root
        res = None

        while node:
            if node.val > val:
                res = node
                node = node.left
            else:
                node = node.right

        if res:
            print(res.val)
        else:
            print('None')
        return res

a = BST()
a.insert(3)
a.insert(1)
a.insert(2)
a.insert(4)
print(a.search(1))
print(a.search(-1))
a.successor(3)
a.delete(4)
a.print()
