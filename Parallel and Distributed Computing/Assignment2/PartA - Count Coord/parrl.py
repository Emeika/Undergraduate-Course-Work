import time
import multiprocessing


def is_in_A(x, y):
    return (x > 0 and (y >= 0 or y == 0) and y >= x) or (x == 0 and y == 0)


def is_in_B(x, y):
    return x > 0 and (y > 0 or y == 0) and y < x


def is_in_C(x, y):
    return x > 0 and y < 0 and y <= -x


def is_in_D(x, y):
    return (x > 0 and y < 0 and y > -x) or (x == 0 and y < 0)


def is_in_E(x, y):
    return x < 0 and y < 0 and y >= x


def is_in_F(x, y):
    return (x < 0 and y < 0 and y < x) or (x < 0 and y == 0)


def is_in_G(x, y):
    return (x < 0 or x == 0) and y > 0 and y <= -x


def is_in_H(x, y):
    return (x < 0 or x == 0) and y > 0 and y > -x


def count_coords(lines):
    counts = {'A part': 0,
              'B part': 0,
              'C part': 0,
              'D part': 0,
              'E part': 0,
              'F part': 0,
              'G part': 0,
              'H part': 0}

    for line in lines:
        x, y = map(int, line.split(','))
        if is_in_A(x, y):
            counts['A part'] += 1
        elif is_in_B(x, y):
            counts['B part'] += 1
        elif is_in_C(x, y):
            counts['C part'] += 1
        elif is_in_D(x, y):
            counts['D part'] += 1
        elif is_in_E(x, y):
            counts['E part'] += 1
        elif is_in_F(x, y):
            counts['F part'] += 1
        elif is_in_G(x, y):
            counts['G part'] += 1
        elif is_in_H(x, y):
            counts['H part'] += 1

    return counts


if __name__ == '__main__':
    start_time = time.time()
    filename = 'coordinate_points.txt'

    # Read the file and split it into chunks
    with open(filename, 'r') as file:
        lines = file.readlines()
    chunks = [lines[i:i + 1000] for i in range(0, len(lines), 1000)]

    # Use multiprocessing Pool to parallelize the process
    # 12 PROCESSES
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(count_coords, chunks)

    # Combine the results from each process
    counts = {'A part': 0,
              'B part': 0,
              'C part': 0,
              'D part': 0,
              'E part': 0,
              'F part': 0,
              'G part': 0,
              'H part': 0}
    for result in results:
        for part, count in result.items():
            counts[part] += count

    total = sum(counts.values())

    for part, count in counts.items():
        print(f'{part}: {count}')
    print(f"Total coordinates: {total}")
    print(f'Execution time: {time.time() - start_time} seconds')
