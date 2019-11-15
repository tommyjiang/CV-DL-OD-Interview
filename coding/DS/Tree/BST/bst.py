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
        node = self.search(val)
        if not node:
            print('No such node.')
            return False
        else:
            self._delete(val, self.root)  # also search from root
            return True


    def _delete(self, val, node):
        if not node:
            return None
        if node.val == val:
            # replace node with node.right's left most node
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


    def inorder_recur(self, node):
        if not node:
            return
        self.inorder_recur(node.left)
        print(node.val)
        self.inorder_recur(node.right)


    def inorder_iter(self):
        node = self.root
        s = []

        while node or s:
            while node:
                s.append(node)
                node = node.left

            if s:
                node = s.pop()
                print(node.val)
                node = node.right


    def print_inorder(self):
        # self.inorder_recur(self.root)
        self.inorder_iter()


    def preorder_iter(self):
        node = self.root
        s = []

        while node or s:
            while node:
                print(node.val)
                s.append(node)
                node = node.left

            if s:
                node = s.pop()
                node = node.right

    def print_preorder(self):
        self.preorder_iter()


    def successor_root(self, val):
        node = self.root
        res = None

        while node:
            if node.val > val:
                res = node
                node = node.left
            else:
                node = node.right

        return res


    def successor_parent(self, val):
        node = self.search(val)
        if not node:
            return None
        else:
            if node.right:
                node = node.right
                while node.right:
                    node = node.right
                return node
            else:
                while node.p:
                    if node == node.p.left:
                        return node.p
                    else:
                        node = node.p
                return None


a = BST()
a.insert(3)
a.insert(1)
a.insert(2)
a.insert(4)
a.print_inorder()
a.print_preorder()
# print(a.search(1))
# print(a.search(-1))
# a.successor_root(3)
# a.delete(4)
