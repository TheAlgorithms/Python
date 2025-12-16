class Node:  
    def __init__(self, data):  
        self.data = data  
        self.left = None  
        self.right = None  

# Function to insert a new node in the BST  
def insert(root, data):  
    if root is None:  
        return Node(data)  
    if data < root.data:  
        root.left = insert(root.left, data)  
    else:  
        root.right = insert(root.right, data)  
    return root  

# Function to perform in-order traversal of the BST  
def in_order_traversal(root):  
    if root is not None:  
        in_order_traversal(root.left)  
        print(root.data, end=' ')  
        in_order_traversal(root.right)  

# Function to find the minimum value node in a given subtree  
def min_value_node(node):  
    current = node  
    while current and current.left is not None:  
        current = current.left  
    return current  

# Function to delete a node from the BST  
def delete_node(root, key):  
    if root is None:  
        return root  

    if key < root.data:  
        root.left = delete_node(root.left, key)  
    elif key > root.data:  
        root.right = delete_node(root.right, key)  
    else:  
        # Node with only one child or no child  
        if root.left is None:  
            temp = root.right  
            root = None  # Clear the node  
            return temp  
        elif root.right is None:  
            temp = root.left  
            root = None  # Clear the node  
            return temp  

        # Node with two children: get the inorder successor  
        temp = min_value_node(root.right)  
        root.data = temp.data  
        root.right = delete_node(root.right, temp.data)  

    return root  

def main():  
    root = None  

    # Inserting nodes into the BST  
    root = insert(root, 50)  
    insert(root, 30)  
    insert(root, 20)  
    insert(root, 40)  
    insert(root, 70)  
    insert(root, 60)  
    insert(root, 80)  

    print("Inorder Traversal of the BST before deletion:")  
    in_order_traversal(root)  
    print("\n")  

    # Deleting a node  
    key = int(input("Enter the Key Element to be deleted: "))  
    root = delete_node(root, key)  
    print(f"Element ({key}) Deleted")  
    print(f"Inorder Traversal of the BST after deletion of {key}:")  
    in_order_traversal(root)  
    print("\n")  

if __name__ == "__main__":  
    main()