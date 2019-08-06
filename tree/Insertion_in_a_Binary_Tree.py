#creating node
class node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(temp):

    if (not temp):
        return

    inorder(temp.left)
    print(temp.data,end = " ")
    inorder(temp.right)



def build_tree():
    print("\n********Press N to stop entering at any point of time********\n")
    print("Enter the value of the root node: ", end="")
    check = input().strip().lower()
    if check == 'n':
        return None
    data = int(check)

    temp = node(data)

    q=[]
    q.append(temp)
    #level order traversal until we find empty place
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = node(data)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = node(data)
            break
        else:
            q.append(temp.right)



def insert(temp,data):
    """function to insert element in binary tree
       using level order traversal

       """

    q=[]
    q.append(temp)
    #level order traversal until we find empty place
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = node(data)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = node(data)
            break
        else:
            q.append(temp.right)


if __name__ == '__main__':

    """ to make a basic tree """

    root = node(10)
    root.left = node(11)
    root.left.left = node(7)
    root.right = node(9)
    root.right.left = node(15)
    root.right.right = node(8)


    data = int(input().strip())

    insert(root, data)

    inorder(root)
