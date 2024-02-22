# Custom queue implementation in Python
class Queue:

    # Initialize queue
    def __init__(self, size=1000):
        self.q = [None] * size      # list to store queue elements
        self.capacity = size        # maximum capacity of the queue
        self.front = 0              # front points to the front element in the queue
        self.rear = -1              # rear points to the last element in the queue
        self.count = 0              # current size of the queue

    # Function to dequeue the front element
    def dequeue(self):
        # check for queue underflow
        if self.isEmpty():
            print('Queue Underflow!! Terminating process.')
            exit(-1)
        x = self.q[self.front]
        print('Removing element…', x)
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
        return x

    # Function to add an element to the queue
    def enqueue(self, value):
        # check for queue overflow
        if self.isFull():
            print('Overflow!! Terminating process.')
            exit(-1)
        print('Inserting element…', value)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    # Function to return the front element of the queue
    def peek(self):
        if self.isEmpty():
            print('Queue Underflow!! Terminating process.')
            exit(-1)
        return self.q[self.front]
    # Function to return the size of the queue

    def size(self):
        # Function to check if the queue is empty or not
        return self.count

    def isEmpty(self):
        # Function to check if the queue is full or not
        if self.count == 0:
            return True
        return False

    def isFull(self):
        if self.count == self.capacity:
            return True
        return False


if __name__ == '__main__':
    # create a queue of capacity 5
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print('The queue size is', q.size())
    print('The front element is', q.peek())
    q.dequeue()
    print('The front element is', q.peek())
    q.dequeue()
    q.dequeue()
    if q.isEmpty():
        print('The queue is empty')
    else:
        print('The queue is not empty')
