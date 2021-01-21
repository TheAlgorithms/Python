# Absolute Value :

def abs_val(num):
    return -num if num < 0 else num

def test_abs_val():
    assert 0 == abs_val(0)
    assert 45 == abs_val(45)
    assert 100000000 == abs_val(-100000000)
    
if __name__ == "__main__":
    num = int(input("Enter a number : "))
    print(abs_val(num))

