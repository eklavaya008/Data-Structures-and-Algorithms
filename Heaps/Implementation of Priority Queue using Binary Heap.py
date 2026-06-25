class MaxHeap:
    def __init__(self):
        self.H = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def shiftUp(self, i):
        while i > 0 and self.H[self.parent(i)] < self.H[i]:
            p = self.parent(i)
            self.H[i], self.H[p] = self.H[p], self.H[i]
            i = p

    def shiftDown(self, i):
        n = len(self.H)

        while True:
            largest = i
            left = self.leftChild(i)
            right = self.rightChild(i)

            if left < n and self.H[left] > self.H[largest]:
                largest = left

            if right < n and self.H[right] > self.H[largest]:
                largest = right

            if largest == i:
                break

            self.H[i], self.H[largest] = self.H[largest], self.H[i]
            i = largest

    def insert(self, value):
        self.H.append(value)
        self.shiftUp(len(self.H) - 1)

    def extractMax(self):
        if not self.H:
            return -1

        maximum = self.H[0]

        if len(self.H) == 1:
            self.H.pop()
            return maximum

        self.H[0] = self.H.pop()
        self.shiftDown(0)

        return maximum


# Example usage
heap = MaxHeap()
heap.insert(75)
heap.insert(26)

print("Node with maximum priority :", heap.extractMax())
print("Priority queue after extracting maximum :", *heap.H)