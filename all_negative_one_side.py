

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        gr = []
        lr = []
        for i in range(len(arr)):
            if arr[i] >= 0:
                gr.append(arr[i])
            else:
                lr.append(arr[i])
        for i in range(len(gr)):
            arr[i] = gr[i]
        for i in range(len(lr)):
            arr[i + len(gr)] = lr[i]





def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()

