# Question 4: [Weightage: 60%]
# Implement Round Robin Scheduling Algorithm using Queues.

from CircularQueue import CircularQueue

times = [1,3,6,2,6,8]

queue = CircularQueue()

for i in times:
    queue.enqueue(i)

allocation = 3

point = 0
step = 0

while not queue.is_empty():

    if point == len(times):
        point = 0

    times[point] = (queue.dequeue() - allocation)

    print('Dequeueing')
    print(queue.get_data())   # to print the data in the list - made a getter in queue class
    print()

    step += 1

    if times[point] > 0:
        queue.enqueue(times[point])

        print('Enqueueing')
        print(queue.get_data())
        print()

        step += 1

    point += 1

print('Steps: ', step)

