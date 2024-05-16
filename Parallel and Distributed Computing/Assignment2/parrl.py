import time
import multiprocessing
from collections import defaultdict


def check_point_part(point):
    x, y = point
    if x > 0 and y > 0:
        return 'A PART'
    elif x < 0 and y > 0:
        return 'B PART'
    elif x < 0 and y < 0:
        return 'C PART'
    elif x > 0 and y < 0:
        return 'D PART'
    elif x > 0 and y == 0:
        return 'E PART'
    elif x < 0 and y == 0:
        return 'F PART'
    elif x == 0 and y > 0:
        return 'G PART'
    elif x == 0 and y < 0:
        return 'H PART'
    else:  # The point is at the origin (0, 0)
        return 'Origin'


def worker(points, queue):
    counts = defaultdict(int)
    for point in points:
        part = check_point_part(point)
        counts[part] += 1
    queue.put(counts)


def count_points_in_parts(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.split(','))
            points.append((x, y))

    # Divide the points into chunks for each worker
    num_workers = multiprocessing.cpu_count()
    chunks = [points[i::num_workers] for i in range(num_workers)]

    # Create a queue to collect the results
    queue = multiprocessing.Queue()

    # Start the workers
    workers = []
    for chunk in chunks:
        worker_process = multiprocessing.Process(
            target=worker, args=(chunk, queue))
        worker_process.start()
        workers.append(worker_process)

    # Wait for all workers to finish
    for worker_process in workers:
        worker_process.join()

    # Combine the results from all workers
    counts = defaultdict(int)
    while not queue.empty():
        worker_counts = queue.get()
        for part, count in worker_counts.items():
            counts[part] += count

    return counts


if __name__ == '__main__':
    start_time = time.time()

    filename = 'coordinate_points.txt'  # Replace with the actual filename
    counts = count_points_in_parts(filename)

    for part, count in counts.items():
        print(f'{part}: {count}')

    end_time = time.time()
    print(f'Execution time: {end_time - start_time} seconds')
