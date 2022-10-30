def search_quadruplets(sequence: list[int], target: int) -> list[int]:
    """
    >>> search_quadruplets([4, 1, 2, -1, 1, -3], 1)

    [-3, -1, 1, 4], [-3, 1, 1, 2]
    Explanation: Both the quadruplets add up to the target.

    >>> search_quadruplets([2, 0, -1, 1, -2, 2], 2)
    [-2, 0, 2, 2], [-1, 0, 1, 2]
    Explanation: Both the quadruplets add up to the target.

    Technique: Two Pointers
    This problem follows the Two Pointers pattern and
    shares similarities with Triplet Sum to Zero.

    """

    sequence.sort()
    quadruplets = []
    for index in range(0, len(sequence) - 3):
        if index > 0 and sequence[index] == sequence[index - 1]:
            continue
        for another_index in range(index + 1, len(sequence) - 2):
            if (
                another_index > 0
                and sequence[another_index] == sequence[another_index - 1]
            ):
                continue

            left = another_index + 1
            right = len(sequence) - 1
            while left < right:
                quadruplets_sum = (
                    sequence[index]
                    + sequence[another_index]
                    + sequence[left]
                    + sequence[right]
                )
                if quadruplets_sum == target:
                    quadruplets.append(
                        [
                            sequence[index],
                            sequence[another_index],
                            sequence[left],
                            sequence[right],
                        ]
                    )
                    left += 1
                    right -= 1

                    while left < right and sequence[left] == sequence[left - 1]:
                        left += 1
                    while left < right and sequence[right] == sequence[right + 1]:
                        right -= 1
                elif quadruplets_sum < target:
                    left += 1
                else:
                    right -= 1
    return quadruplets


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item) for item in user_input.split(",")]

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = search_quadruplets(sequence, target)
    if result is not None:
        print(f"result: {result}")
    else:
        print("Not found")
