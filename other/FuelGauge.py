def main():
    text = input("Enter:")
    con = convert(text)
    print(con)
    gau = gauge(con)
    print(gau)


def convert(fraction):
    while True:
        try:
            a, b = fraction.split("/")
            new_a = int(a)
            new_b = int(b)
            ans = new_a / new_b

            if ans <= 1:
                p = int(ans * 100)
                return p
            else:
                fraction = input("Fraction:")
                pass

        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1 and percentage >= 0:
        return "E"
    elif percentage >= 99 and percentage <=100:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
