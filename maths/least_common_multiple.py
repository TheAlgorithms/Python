from greater_common_divisor import gcd



def lcm(a, b):
   """This function takes two
   integers and returns the largest common multiple"""
   lcm = (a*b)//gcd(a,b)
   return lcm


def main():
    try:
        nums = input("Enter two Integers separated by comma (,): ").split(',')
        num1 = int(nums[0]); num2 = int(nums[1])
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong Input")
    print(f"lcm({num1}, {num2}) = {lcm(num1, num2)}")

if __name__ == '__main__':
    main()
