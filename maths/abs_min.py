class abshead:
    def abs_min(self, x: list[int]) -> int:
        
        if len(x) == 0:
            raise ValueError("abs_min() arg is an empty sequence")
        j = x[0]
        for i in x:
            if abs(i) < abs(j):
                j = i
        return j

a1 = abshead()

def main():
    a = [-3, -4, 2, -1, -11]
    print(a1.abs_min(a))  # abs_min = -1


if __name__ == "__main__":
    main()
