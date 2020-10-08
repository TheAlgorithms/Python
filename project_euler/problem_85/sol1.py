import math


def solution() -> int:
    goal = 8000000
    root = int(math.sqrt(8000000) + 1)
    distance, resa, resb = goal, 0, 0

    for a in range(1, root + 1):
        for b in range(1, math.ceil(root / a) + 1):
            current_distance = abs((a * b + a) * (a * b + b) - goal)
            if current_distance < distance:
                distance = current_distance
                resa, resb = a, b

    return resa * resb


if __name__ == "__main__":
    print("Area of the grid is ", solution())
