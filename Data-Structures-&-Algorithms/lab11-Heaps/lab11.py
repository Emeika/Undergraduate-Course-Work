class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def Enqueue(self, key, value):
        self.heap.append((key, value))
        self.upheap(len(self.heap)-1)

    def Dequeue(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.downheap(0)
        return min_val

    def downheap(self, index):
        left = self.getleft(index)
        right = self.getright(index)
        smallest = index
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.downheap(smallest)

    def upheap(self, index):
        parent = self.GetParent(index)
        if parent is not None and self.heap[parent][0] > self.heap[index][0]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.upheap(parent)

    def min(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def getright(self, index):
        return (index+1)*2

    def getleft (self, index):
        return (index+1)*2-1

    def GetParent(self, index):
        if index == 0:
            return None
        return (index-1)//2

    def __len__(self):
        return len(self.heap)


# Question 3.
# Write a code to sort an array by using heap sort algorithm.

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print("%d" %arr[i])