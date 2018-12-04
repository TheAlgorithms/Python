# Greater Common Divisor - https://en.wikipedia.org/wiki/Greatest_common_divisor
def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)

def main():
    try:
        nums = input("Enter two Integers separated by comma (,): ").split(',')
        num1 = int(nums[0]); num2 = int(nums[1])
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong Input")
    print(f"gcd({num1}, {num2}) = {gcd(num1, num2)}")

if __name__ == '__main__':
    main()

