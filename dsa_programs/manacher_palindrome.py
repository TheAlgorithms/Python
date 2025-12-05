"""Manacher's algorithm for longest palindromic substring."""


def manacher_longest_palindrome(text: str) -> str:
    if not text:
        return ""
    transformed = "|" + "|".join(text) + "|"
    center = right = 0
    radii = [0] * len(transformed)
    best_center = best_radius = 0
    for idx in range(len(transformed)):
        mirror = 2 * center - idx
        if idx < right:
            radii[idx] = min(right - idx, radii[mirror])
        while (
            idx - radii[idx] - 1 >= 0
            and idx + radii[idx] + 1 < len(transformed)
            and transformed[idx - radii[idx] - 1] == transformed[idx + radii[idx] + 1]
        ):
            radii[idx] += 1
        if idx + radii[idx] > right:
            center = idx
            right = idx + radii[idx]
        if radii[idx] > best_radius:
            best_center = idx
            best_radius = radii[idx]
    start = (best_center - best_radius) // 2
    end = start + best_radius
    return text[start:end]
