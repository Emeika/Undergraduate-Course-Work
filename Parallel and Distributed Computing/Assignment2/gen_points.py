import random
random.seed(42)

coordinate_points = [(random.randint(-5, 5), random.randint(-5, 5))
                     for _ in range(10000000)]

with open("coordinate_points.txt", "w") as file:
    for point in coordinate_points:
        file.write(f"{point[0]},{point[1]}\n")

print("Coordinate points written to coordinate_points.txt")
