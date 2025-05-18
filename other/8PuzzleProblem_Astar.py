import copy
import heapq

class Puzzle:
    
    def __init__(self, initial_state):
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.initial_state = initial_state
        self.open_list = []
        self.closed_list = []
    
    def get_heuristic(self, state):
        heuristic = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    x_goal, y_goal = divmod(state[i][j] - 1, 3)
                    heuristic += abs(i - x_goal) + abs(j - y_goal)
        return heuristic
    
    def get_blank_position(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)
    
    def get_successors(self, state):
        successors = []
        i_blank, j_blank = self.get_blank_position(state)
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= i_blank + x < 3 and 0 <= j_blank + y < 3:
                new_state = copy.deepcopy(state)
                new_state[i_blank][j_blank], new_state[i_blank + x][j_blank + y] = new_state[i_blank + x][j_blank + y], new_state[i_blank][j_blank]
                successors.append(new_state)
        return successors
    
    def solve(self):
        start_node = (self.get_heuristic(self.initial_state), self.initial_state, 0, None)
        heapq.heappush(self.open_list, start_node)
        
        while self.open_list:
            current_node = heapq.heappop(self.open_list)
            current_cost = current_node[2]
            current_state = current_node[1]
            
            if current_state == self.goal_state:
                path = []
                while current_node:
                    path.append(current_node[1])
                    current_node = current_node[3]
                return reversed(path)
            
            self.closed_list.append(current_state)
            successors = self.get_successors(current_state)
            for successor in successors:
                if successor not in self.closed_list:
                    g_cost = current_cost + 1
                    h_cost = self.get_heuristic(successor)
                    f_cost = g_cost + h_cost
                    new_node = (f_cost, successor, g_cost, current_node)
                    heapq.heappush(self.open_list, new_node)
        
        return None

# Run the Solver
initial_state = [[1,2, 3], [4,5,6], [0,7,8]]
solver = Puzzle(initial_state)
solution = solver.solve()

if solution:
    for idx, state in enumerate(solution):
        print(f"Move {idx + 1}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")