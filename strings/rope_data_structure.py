# This is a Rope Data Structure for fast string concatination using Rope Structure method
# This code defines a rope data structure and functions to create, print, and concatenate ropes. It then creates two ropes for input strings 'a' and 'b', concatenates them into 'root3', and prints the concatenated result.
# Expected output :   Input  : a[] = "Hi ", b[] = "There !"
#                     Output : "Hi There !"
# Time Complexity: O(1)
# Auxiliary Space: O(1)
# refrence links : wikipedia = "https://en.wikipedia.org/wiki/Rope_(data_structure)"
#                  geeks for geeks = "https://www.geeksforgeeks.org/ropes-data-structure-fast-string-concatenation/"


LEAF_LEN = 2  # Define a constant for the maximum number of characters in leaf nodes


class Rope:  # Define a class called 'Rope' for a rope data structure
    def __init__(self):  # Define a constructor for the 'Rope' class
        self.left = None  # Initialize the left child of the node as None
        self.right = None  # Initialize the right child of the node as None
        self.parent = None  # Initialize the parent of the node as None
        self.str = [0] * (LEAF_LEN + 1)  # Initialize a list of characters with zeros
        self.lCount = 0  # Initialize the character count as 0


def createRopeStructure(
    node, par, a, l, r
):  # Define a function to create a rope structure
    tmp = Rope()  # Create a temporary 'Rope' object
    tmp.left = tmp.right = None  # Initialize left and right children as None
    tmp.parent = par  # Set the parent of the node

    if (r - l) > LEAF_LEN:  # If the length of the substring is greater than LEAF_LEN
        tmp.str = None  # Set the character string of the node as None
        tmp.lCount = (r - l) // 2  # Calculate and set the left character count
        node = tmp  # Set the current node as 'tmp'
        m = (l + r) // 2  # Calculate the midpoint of the substring
        createRopeStructure(
            node.left, node, a, l, m
        )  # Recursively create the left subtree
        createRopeStructure(
            node.right, node, a, m + 1, r
        )  # Recursively create the right subtree
    else:
        node = tmp  # Set the current node as 'tmp'
        tmp.lCount = r - l  # Set the character count
        j = 0
        for i in range(l, r + 1):  # Iterate through the substring indices
            print(a[i], end="")  # Print the character
            tmp.str[j] = a[i]  # Store the character in the node's character list
            j = j + 1  # Increment the index
        print(end="")  # Print an empty line

    return node  # Return the constructed node


def printstring(r):  # Define a function to print the string (leaf nodes)
    if r == None:  # If the node is None, return
        return

    if r.left == None and r.right == None:  # If the node is a leaf node
        pass

    printstring(r.left)  # Recursively print the left subtree
    printstring(r.right)  # Recursively print the right subtree


def concatenate(
    root3, root1, root2, n1
):  # Define a function to efficiently concatenate two strings
    tmp = Rope()  # Create a temporary 'Rope' object
    tmp.left = root1  # Set 'root1' as the left child
    tmp.right = root2  # Set 'root2' as the right child
    root1.parent = tmp  # Set 'tmp' as the parent of 'root1'
    root2.parent = tmp  # Set 'tmp' as the parent of 'root2'
    tmp.lCount = n1  # Set the character count of 'tmp'

    tmp.str = None  # Set the character string of 'tmp' as None
    root3 = tmp  # Set 'tmp' as 'root3'

    return root3  # Return the concatenated rope


root1 = None  # Initialize 'root1' as None
a = "Hello , This is Rope Data Structure "  # Define a string 'a'
n1 = len(a)  # Calculate the length of string 'a' and store it in 'n1'
root1 = createRopeStructure(
    root1, None, a, 0, n1 - 1
)  # Create a rope structure for string 'a'

root2 = None  # Initialize 'root2' as None
b = ", Used to Concatinate Two Strings"  # Define a string 'b'
n2 = len(b)  # Calculate the length of string 'b' and store it in 'n2'
root2 = createRopeStructure(
    root2, None, b, 0, n2 - 1
)  # Create a rope structure for string 'b'

root3 = None  # Initialize 'root3' as None
root3 = concatenate(root3, root1, root2, n1)  # Concatenate the two ropes into 'root3'

printstring(root3)  # Print the concatenated string
print()  # Print an empty line
