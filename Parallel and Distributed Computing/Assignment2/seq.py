import time


def count_coords(filename):
    counts = {'A part': 0,
              'B part': 0,
              'C part': 0,
              'D part': 0,
              'E part': 0,
              'F part': 0,
              'G part': 0,
              'H part': 0, }

    with open(filename, 'r') as file:
        for line in file:
            x, y = map(int, line.split(','))

            if x > 0 and (y > 0 or y == 0):  # 3, 0 go to else
                if y >= x:
                    counts['A part'] += 1
                else:
                    counts['B part'] += 1

            elif x > 0 and y < 0:
                if y <= -x:
                    counts['C part'] += 1
                else:
                    counts['D part'] += 1

            elif (x < 0 and y < 0):  # -1 -1
                if y >= x:
                    counts['E part'] += 1
                else:
                    counts['F part'] += 1

            elif (x < 0 or x == 0) and y > 0:   # 0, 3 go to else
                if y > -x:                                   # -3, 3
                    counts['H part'] += 1
                else:
                    counts['G part'] += 1

            elif x == 0 and y < 0:  # 0, -3
                counts['D part'] += 1

            elif x < 0 and y == 0:  # -1, 0
                counts['F part'] += 1

            elif x == 0 and y == 0:
                counts['A part'] += 1

    return counts


start_time = time.time()

filename = 'coordinate_points.txt'
counts = count_coords(filename)

total = 0
for part, count in counts.items():
    print(f'{part}: {count}')
    total += count

end_time = time.time()

print(f"Total coordinates: {total}")
print(f'Execution time: {end_time - start_time} seconds')
