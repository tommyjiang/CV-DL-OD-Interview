class min_heap():
    def __init__(self, A=[]):
        self._data = A
        self._size = len(A)
        self.heapify()

    def _up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self._data[idx] < self._data[parent]:
                self._data[idx], self._data[parent] = self._data[parent], self._data[idx]
                idx = parent

    def _down(self, idx):
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left >= self._size:
                return
            elif left == self._size-1:
                if self._data[left] < self._data[idx]:
                    self._data[left], self._data[idx] = self._data[idx], self._data[left]
                return
            elif left < self._size-1:
                if self._data[left] <= self._data[smallest] and self._data[left] <= self._data[right]:
                    smallest = left
                elif self._data[right] <= self._data[smallest] and self._data[right] <= self._data[left]:
                    smallest = right
                if smallest != idx:
                    self._data[idx], self._data[smallest] = self._data[smallest], self._data[idx]
                    idx = smallest
                else:
                    return

    def insert(self, value):
        self._data[self._size] = value
        self._size += 1
        self._up(self._size-1)

    def pop(self):
        if self._size == 0:
            return

        value = self._data[0]
        self._data[0] = self._data[self._size-1]
        self._data.pop(self._size-1)
        self._size -= 1
        self._down(0)
        return value

    def heapify(self):
        for i in range(self._size//2, -1, -1):
            self._down(i)

A = [1, 6, 2, 2, 5, 4, 7, 8, 3, 9, 0]
a = min_heap()
