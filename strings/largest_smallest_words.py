""" 
To find the smallest and largest word in the sentence
Example 
    if the input string is 
    My name is abc
    then the output will be
    The smallest word in the given string is be
    The largest word in the given string is output
"""

def find_smallest_and_largest_words(input_string):
    words = input_string.split()
    if not words:
        return None, None

    smallest_word = min(words, key=len)
    largest_word = max(words, key=len)

    return smallest_word, largest_word

if __name__ == "__main__":
    input_string = input("Enter a string here:\n").strip()
    smallest, largest = find_smallest_and_largest_words(input_string)

    if smallest is not None and largest is not None:
        print(f"The smallest word in the given string is {smallest}")
        print(f"The largest word in the given string is {largest}")
    else:
        print("No words found in the input string.")
