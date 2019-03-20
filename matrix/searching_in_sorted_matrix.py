def search_in_a_sorted_matrix(mat, m, n, key):
    i, j = m - 1, 0
    while i >= 0 and j < n:
        if key == mat[i][j]:
            print('Key %s found at row- %s column- %s' % (key, i + 1, j + 1))
            return
        if key < mat[i][j]:
            i -= 1
        else:
            j += 1
    print('Key %s not found' % (key))


def main():
    mat = [
        [2, 5, 7],
        [4, 8, 13],
        [9, 11, 15],
        [12, 17, 20]
    ]
    x = int(input("Enter the element to be searched:"))
    print(mat)
    search_in_a_sorted_matrix(mat, len(mat), len(mat[0]), x)


if __name__ == '__main__':
    main()
