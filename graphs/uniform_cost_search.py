class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        if data not in self.queue:
            self.queue.append(data)

    def get(self):
        try:
            min_value = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min_value][0]:
                    min_value = i
            item = self.queue[min_value]
            return item
        except IndexError:
            return

    def delete_data(self, data):
        try:
            min_value = 0
            for i in range(len(self.queue)):
                if self.queue[i] == data:
                    min_value = i
            del self.queue[min_value]
        except IndexError:
            return


def node_cost(cost, from_node, to_node):
    k = 0
    costval = 0
    for i in cost:
        for j in range(len(i)):
            if from_node == k and to_node == j:
                costval = i[j]
                return costval
            else:
                continue
        k += 1
    return costval


def UCS_Traversal(graph, start, goal):

    path = []
    visited = set()

    if start in goal:
        return path
    if start not in range(len(graph)):
        return

    frontier = PriorityQueue()
    path.append(start)
    path_cost = 0
    frontier.insert([path_cost, path])

    while not frontier.isEmpty():

        current_node_val = frontier.get()
        path_cost_till_now = current_node_val[0]
        path_till_now = current_node_val[1]
        current_node = path_till_now[-1]

        visited.add(current_node)

        if current_node in goal:
            return path_till_now

        children_of_current = graph[current_node]
        frontier.delete_data(current_node)

        for child_node in range(0, len(children_of_current)):
            if child_node not in visited:
                if children_of_current[child_node] > 0:
                    path_to_child = path_till_now.copy()
                    path_to_child.append(child_node)
                    cost_of_child = (
                        node_cost(graph, current_node, child_node) + path_cost_till_now
                    )
                    new_element = [cost_of_child, path_to_child]
                    frontier.insert(new_element)

    return path_till_now


cost = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 9, -1, 6, -1, -1, -1, -1, -1],
    [0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1],
    [0, -1, 2, 0, 1, -1, -1, -1, -1, -1, -1],
    [0, 6, -1, -1, 0, -1, -1, 5, 7, -1, -1],
    [0, -1, -1, -1, 2, 0, -1, -1, -1, 2, -1],
    [0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
    [0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1],
    [0, -1, -1, -1, -1, 2, -1, -1, 0, -1, 8],
    [0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 7],
    [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0],
]

print(UCS_Traversal(cost, 1, [6, 7, 10]))
