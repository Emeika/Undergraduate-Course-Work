class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(value)

    def get(self, index):
        cur = self.head
        for _ in range(index):
            if not cur:
                return None
            cur = cur.next
        return cur.value if cur else None

    def set(self, index, value):
        cur = self.head
        for _ in range(index):
            if not cur:
                return
            cur = cur.next
        if cur:
            cur.value = value

    def print(self):
        cur = self.head
        while cur:
            print(cur.value, end=" ")
            cur = cur.next
        print()

class Item:
    def __init__(self, cost=0, is_kept=0):
        self.cost = cost
        self.is_kept = is_kept

def KnapSack(row_n, max_capacity, values, weights, dp, items):
    if row_n == 0:
        return 0
    if weights[row_n-1] > max_capacity:
        if dp.get(row_n-1).get(max_capacity) == -1:
            dp.get(row_n).set(max_capacity, KnapSack(row_n-1, max_capacity, values, weights, dp, items))
        return dp.get(row_n).get(max_capacity)
    else:
        if dp.get(row_n-1).get(max_capacity) == -1:
            dp.get(row_n).set(max_capacity, KnapSack(row_n-1, max_capacity, values, weights, dp, items))
        if dp.get(row_n-1).get(max_capacity - weights[row_n-1]) == -1:
            dp.get(row_n-1).set(max_capacity - weights[row_n-1], KnapSack(row_n-1, max_capacity - weights[row_n-1], values, weights, dp, items))

        include_item = values[row_n-1] + dp.get(row_n-1).get(max_capacity - weights[row_n-1])
        dp.get(row_n).set(max_capacity, max(dp.get(row_n-1).get(max_capacity), include_item))
        if dp.get(row_n).get(max_capacity) == include_item:
            items[row_n-1].is_kept = 1  # Mark the item as selected

        return dp.get(row_n).get(max_capacity)

def main():
    max_capacity = 11
    weights = [1, 2, 5, 6, 7]
    values = [1, 6, 18, 22, 28]
    row_n = len(values)
    dp = LinkedList()
    for _ in range(row_n + 1):
        row = LinkedList()
        for _ in range(max_capacity + 1):
            row.append(-1)
        dp.append(row)
    items = [Item(cost=values[i], is_kept=0) for i in range(row_n)]

    KnapSack(row_n, max_capacity, values, weights, dp, items)

    print("Dynamic Programming Table:")
    for i in range(row_n + 1):
        dp.get(i).print()

    print("\nItems selected:")
    for i, item in enumerate(items):
        if item.is_kept:
            print(f"Item {i+1} (Weight: {weights[i]}, Value: {values[i]})")

    print(f"\nMax worth of bag of {max_capacity}: {dp.get(row_n).get(max_capacity)}")

if __name__ == '__main__':
    main()
