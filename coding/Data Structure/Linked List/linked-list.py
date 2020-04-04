class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Linked_List:
    def __init__(self, A=None):
        if not A:
            self.head = None
        else:
            self.head = Node(A[0])
            cur = self.head
            for i in range(1, len(A)):
                cur.next = Node(A[i])
                cur = cur.next


    def __repr__(self):
        res = ''
        cur = self.head

        while cur:
            res += str(cur.val) + ' '
            cur = cur.next

        return res

    def reverse_iter(self):
        prev = None
        head = self.head

        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur

        self.head = prev

    def _reverse_recur(self, node, prev=None):
        if not node:
            return prev

        next = node.next
        node.next = prev
        return self._reverse_recur(next, node)

    def reverse_recur(self):
        self.head = self._reverse_recur(self.head)


A = [1, 2, 3, 4, 5]
ll = Linked_List(A)
print(ll)
ll.reverse_iter()
print(ll)
ll.reverse_recur()
print(ll)
