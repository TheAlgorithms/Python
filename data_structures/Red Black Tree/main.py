from Red_Black_Tree import RBTree
r = RBTree()
print('Enter initial elements :')
for ele in list(map(int,input().split())):
    r.insert(ele)
print('1.Insert','2.Inorder','3.Search','4.Delete','5.Display',sep='\n')
while True:
    choice = int(input())
    if choice == 1:
        print('Enter element to be inserted : ',end='')
        r.insert(int(input()))
    elif choice == 2:
        print('Inorder : ',end='')
        r.inorder(r.root)
        print()
    elif choice == 3:
        print('Enter search element : ',end='')
        print(r.search(int(input())))
    elif choice == 4:
        print('Enter element to be deleted : ',end='')
        r.delete(int(input()))
    elif choice == 5:
        if r.root == r.ext:
            print('Tree is empty')
        else:
            print('Root -> ',end='')
            r.display(r.root)
    else:
        break