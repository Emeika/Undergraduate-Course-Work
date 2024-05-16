import time
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


def count_points_in_parts(filename):
    counts = defaultdict(int)

    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.split(','))
            part = check_point_part((x, y))
            counts[part] += 1

    return counts


start_time = time.time()

filename = 'coordinate_points.txt'  # Replace with the actual filename
counts = count_points_in_parts(filename)

for part, count in counts.items():
    print(f'{part}: {count}')

end_time = time.time()
print(f'Execution time: {end_time - start_time} seconds')
