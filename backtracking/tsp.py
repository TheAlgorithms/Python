from itertools import permutations

def calculate_total_distance(points, order):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distance(points[order[i]], points[order[i + 1]])
    total_distance += distance(points[order[-1]], points[order[0]])  # Return to the starting point
    return total_distance

def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

def tsp_bruteforce(points):
    num_points = len(points)
    if num_points < 2:
        return points, 0

    best_order = None
    best_distance = float('inf')

    for order in permutations(range(num_points)):
        current_distance = calculate_total_distance(points, order)
        if current_distance < best_distance:
            best_distance = current_distance
            best_order = order

    best_path = [points[i] for i in best_order]
    return best_path, best_distance

def main():
    num_points = int(input("Enter the number of points: "))
    points = []
    for i in range(num_points):
        x, y = map(float, input(f"Enter the coordinates for point {i+1} (x y): ").split())
        points.append((x, y))

    best_path, best_distance = tsp_bruteforce(points)
    print("Best Path:", best_path)
    print("Total Distance:", best_distance)

if __name__ == '__main__':
    main()
