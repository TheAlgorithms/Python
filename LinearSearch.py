import sys


def sequential_search(alist, target):
    for index, item in enumerate(alist):
        if item == target:
            print("Found target {} at index {}".format(target, index))
            break
    else:
        print("Not found")


def main():
    # Python 2's `raw_input` has been renamed to `input` in Python 3
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    try:
        print("Enter numbers separated by spaces")
        s = input_function()
        inputs = list(map(int, s.split(' ')))
        target = int(input_function('\nEnter a number to be found in list: '))
    except Exception as e:
        print(e)
    else:
        sequential_search(inputs, target)

if __name__ == '__main__':
    print('==== Linear Search ====\n')
    main()
