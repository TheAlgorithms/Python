N = 50000000


def solution(n_limit: int = N) -> int:
    n_sol = [0] * n_limit

    for delta in range(1, (n_limit + 1) // 4):
        for y in range(4 * delta - 1, delta, -1):
            n = y * (4 * delta - y)
            if n >= n_limit:
                break
            n_sol[n] += 1

    ans = 0
    for i in range(n_limit):
        if n_sol[i] == 1:
            ans += 1

    return ans


if __name__ == "__main__":
    print(f"{solution() = }")
