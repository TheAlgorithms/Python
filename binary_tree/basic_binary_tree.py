class Node: # This is the Class Node with constructor that contains data variable to type data and left,right pointers.
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_into_tree(tree, val):
    if tree is None:
        return Node(val)
    else:
        if val < tree.data:
            tree.left = insert_into_tree(tree.left, val)
        elif val > tree.data:
            tree.right = insert_into_tree(tree.right, val)
        else:
            print("Could not insert {} value already exists".format(val))
    return(tree)


def depth_of_tree(tree): #This is the recursive function to find the depth of binary tree.
    if tree is None:
        return 0
    else:
        depth_l_tree = depth_of_tree(tree.left)
        depth_r_tree = depth_of_tree(tree.right)
        if depth_l_tree > depth_r_tree:
            return 1 + depth_l_tree
        else:
            return 1 + depth_r_tree


def is_full_binary_tree(tree): # This functions returns that is it full binary tree or not?
    if tree is None:
        return True
    if (tree.left is None) and (tree.right is None):
        return True
    if (tree.left is not None) and (tree.right is not None):
        return (is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right))
    else:
        return False


def main(): # Main func for testing.
    #empty tree
    tree = None
    #insert nodes with values 1 to 9
    for i in range(1, 10):
        tree = insert_into_tree(tree, i)
    #test print if item exists already
    tree = insert_into_tree(tree, 1)


    print(is_full_binary_tree(tree))
    print(depth_of_tree(tree))


if __name__ == '__main__':
    main()
