from turtle import right


class RedBlackTree:
    RED = 1
    BLACK = 0

    def __init__(self, val, parent, manage) -> None:
        self.val = val
        self.parent: RedBlackTree = parent
        self.manage: RedBlackTreeManage = manage
        self.left = self.manage.nil
        self.right = self.manage.nil
        self.color = RedBlackTree.RED

    @property
    def text(self):
        return "%s:%s" % (['b', 'r'][self.color], 'n' if self.is_nil() else self.val)

    @property
    def uncle(self):
        return self.parent.brother

    @property
    def brother(self):
        if self.is_left():
            return self.parent.right
        if self.is_right():
            return self.parent.left

    def is_nil(self):
        return self.val is None

    def set_left(self, node):
        self.left = node
        node.set_parent(self)

    def set_right(self, node):
        self.right = node
        node.set_parent(self)

    def set_parent(self, node):
        self.parent = node
        if self.parent.is_nil():
            self.manage.set_root(self)

    def rotate_left(self):
        node = self.right
        self.set_right(node.left)
        self.replace_by(node)
        node.set_left(self)

    def rotate_right(self):
        '''
      5                 3      
   3     6            2   5
 2  4        ->      0 1 4 6
0 1       
        '''
        node = self.left
        self.set_left(node.right)
        self.replace_by(node)
        node.set_right(self)

    def replace_by(self, node):
        if self.parent.is_nil():
            self.manage.set_root(node)
        elif self.is_left():
            self.parent.set_left(node)
        elif self.is_right():
            self.parent.set_right(node)
        node.parent = self.parent

    def is_left(self):
        return self.parent.left == self

    def is_right(self):
        return self.parent.right == self

    def get_min(self):
        if self.left.is_nil():
            return self
        return self.left.get_min()

    def big(self, val):
        return self.val > val

    def small(self, val):
        return self.val < val

    def is_red(self):
        return self.color == RedBlackTree.RED

    def set_color_red(self):
        if self.is_nil():
            return
        self.color = RedBlackTree.RED

    def set_color_black(self):
        self.color = RedBlackTree.BLACK

    def is_black(self):
        return self.color == RedBlackTree.BLACK


class RedBlackTree(RedBlackTree):

    def insert_repair(self):
        #print(self.text, self.parent.text)
        if self.parent.is_nil():
            self.manage.set_root(self)
            return
        if self.parent.is_red():
            if self.uncle and self.uncle.is_red():
                self.parent.set_color_black()
                self.uncle.set_color_black()
                self.parent.parent.set_color_red()
                self.parent.parent.insert_repair()
            else:
                if self.parent.is_right():
                    if self.is_left():
                        self.parent.rotate_right()
                        self.right.insert_repair()
                    elif self.is_right():
                        self.parent.set_color_black()
                        self.parent.parent.set_color_red()
                        self.parent.parent.rotate_left()
                elif self.parent.is_left():
                    if self.is_right():
                        self.parent.rotate_left()
                        self.left.insert_repair()
                    elif self.is_left():
                        self.parent.set_color_black()
                        self.parent.parent.set_color_red()
                        self.parent.parent.rotate_right()

    def set_left(self, node):
        self.left = node
        node.set_parent(self)

    def set_right(self, node):
        self.right = node
        node.set_parent(self)

    def set_parent(self, node):
        self.parent = node
        if self.parent.is_nil():
            self.manage.set_root(self)

    def rotate_left(self):
        node = self.right
        self.set_right(node.left)
        self.replace_by(node)
        node.set_left(self)

    def rotate_right(self):
        '''
      5                 3      
   3     6            2   5
 2  4        ->      0 1 4 6
0 1       
        '''
        node = self.left
        self.set_left(node.right)
        self.replace_by(node)
        node.set_right(self)

    def replace_by(self, node):
        if self.parent.is_nil():
            self.manage.set_root(node)
        elif self.is_left():
            self.parent.set_left(node)
        elif self.is_right():
            self.parent.set_right(node)
        node.set_parent(self.parent)

    def is_left(self):
        return self.parent.left == self

    def is_right(self):
        return self.parent.right == self

    def insert(self, val):
        if self.is_nil():
            return
        if self.small(val):
            if self.right.is_nil():
                self.right = RedBlackTree(val, self, self.manage)
                self.right.insert_repair()
            else:
                self.right.insert(val)
        elif self.big(val):
            if self.left.is_nil():
                self.left = RedBlackTree(val, self, self.manage)
                self.left.insert_repair()
            else:
                self.left.insert(val)

    def remove_repair(self):
        if self.brother is None:
            return
        if self.brother.is_black():
            if self.brother.left.is_black() and self.brother.right.is_black():
                self.brother.set_color_red()
                if self.parent.is_red():
                    self.parent.set_color_black()
                else:
                    self.parent.remove_repair()
            elif self.brother.is_right():
                if self.brother.right.is_red():
                    self.brother.color = self.parent.color
                    self.brother.right.set_color_black()
                    self.parent.set_color_black()
                    self.parent.rotate_left()
                elif self.brother.left.is_red() and self.brother.right.is_black():
                    self.brother.left.set_color_black()
                    self.brother.set_color_red()
                    self.brother.rotate_right()
                    self.remove_repair()
            elif self.brother.is_left():
                if self.brother.left.is_red():
                    self.brother.color = self.parent.color
                    self.brother.left.set_color_black()
                    self.parent.set_color_black()
                    self.parent.rotate_right()
                elif self.brother.right.is_red() and self.brother.left.is_black():
                    self.brother.right.set_color_black()
                    self.brother.set_color_red()
                    self.brother.rotate_left()
                    self.remove_repair()

        elif self.brother.is_red():
            self.brother.set_color_black()
            self.parent.set_color_red()
            if self.brother.is_right():
                self.parent.rotate_left()
            elif self.brother.is_left():
                self.parent.rotate_right()
            self.remove_repair()

    def remove(self, val):
        # print("remove", self.text, val)
        if self.is_nil():
            return
        elif self.val == val:
            if not self.left.is_nil() and not self.right.is_nil():
                z = self.right.get_min()
                self.val = z.val
                self.right.remove(z.val)
            elif not self.left.is_nil():
                self.replace_by(self.left)
                self.left.set_color_black()
            elif not self.right.is_nil():
                self.replace_by(self.right)
                self.right.set_color_black()
            else:
                if self.is_black():
                    self.remove_repair()
                self.replace_by(self.manage.nil)

        elif self.small(val):
            self.right.remove(val)
        elif self.big(val):
            self.left.remove(val)


class RedBlackTreeManage:
    nil = None

    def __init__(self, val) -> None:
        self.nil = RedBlackTree(None, None, self)
        self.nil.set_color_black()
        self.nil.parent = self.nil
        self.root = RedBlackTree(val, self.nil, self)
        self.root.insert_repair()

    def set_root(self, node: RedBlackTree):
        self.root = node
        node.parent = self.nil
        node.set_color_black()

    def insert(self, val):
        self.root.insert(val)

    def remove(self, val):
        self.root.remove(val)

    def get_err_msg(self):
        if self.root.is_red():
            return "root red"

        class Rt:
            error_msg = ""
            last_leaf_depth = None

        def util(node: RedBlackTree, depth):
            if Rt.error_msg:
                return
            if node.parent.is_red() and node.is_red():
                Rt.error_msg = "parent and son is red"
                return
            if node.is_nil():
                depth += 1
                if Rt.last_leaf_depth is not None and Rt.last_leaf_depth != depth:
                    Rt.error_msg = "depth err %s==%s" % (
                        Rt.last_leaf_depth, depth)
                Rt.last_leaf_depth = depth
            else:
                if node.is_black():
                    depth += 1
                util(node.left, depth)
                util(node.right, depth)
        util(self.root, 0)
        return Rt.error_msg

    def to_str(self):
        split_line = '-------------------'
        rt = [split_line]

        def util(node: RedBlackTree, indent):
            if node is None:
                return
            # if node.is_nil():
            #     rt.append("%s%s:%s" %
            #               (' '*indent, 'r' if node.color else 'b', node.text))
            #     return
            util(node.right, indent+4)
            rt.append("%s%s" %
                      (' '*indent, node.text))
            util(node.left, indent+4)
        util(self.root, 0)
        rt.append(split_line)
        return "\n".join(rt)


def tree_insert_remove(rb_insert_array, rb_remove_array, index=0):
    tree = RedBlackTreeManage(rb_insert_array[0])

    def util(method, array):
        for i, value in enumerate(array):
            last_state = tree.to_str()
            if method == "insert":
                tree.insert(value)
            else:
                tree.remove(value)
            err_msg = tree.get_err_msg()
            if err_msg:
                print(last_state)
                print("%s v:%s e:%s" %
                      (method, value, err_msg))
                print(tree.to_str())
                print(index, rb_insert_array, ',', rb_remove_array)
                exit()
    util("insert", rb_insert_array)
    util("remove", rb_remove_array)
    if index == -1:
        print(tree.to_str())


def test_rbtree():
    from random import randint

    def rand_array(array):
        rt = []
        while len(array):
            index = randint(0, len(array)-1)
            rt.append(array.pop(index))
        return rt
    rb_insert_array = rand_array(list(range(0, 20)))
    rb_remove_array = rand_array(list(range(0, 20)))
    tree_insert_remove(rb_insert_array, rb_remove_array)


def test_view():
    tree_insert_remove([1, 3, 10, 12, 6, 8, 9, 2, 4,
                       14, 11, 0, 5, 7, 13], [
        9, 6, 5, 3, 8, 12, 7, 13, 11], -1)
    tree_insert_remove([1, 3, 10, 12, 6, 8, 9, 2, 4,
                       14, 11, 0, 5, 7, 13], [
        9, 6, 5, 3, 8, 12, 7, 13, 10], -1)
    exit()


if __name__ == "__main__":
    # test_view()
    input_case = [
        [0, 3, 1, 4, 5, 2, 6, 7, 9, 8,
         10, 12, 11, 13, 14],
        [4, 0, 8, 9, 1, 11, 2, 3,  12, 13, 5, 6, 7, 10, 14],
        [1, 3, 10, 12, 6, 8, 9, 2, 4, 14, 11, 0, 5, 7, 13], [
            9, 6, 5, 3, 8, 12, 7, 13, 11, 10, 1, 4, 2, 14, 0]
    ]
    for i in range(0, len(input_case), 2):
        tree_insert_remove(input_case[i], input_case[i+1], i//2)
    for i in range(1000):
        test_rbtree()
