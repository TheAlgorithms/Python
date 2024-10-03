# Import PuLP library
from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value

# Create a Linear Programming Minimization problem
prob = LpProblem("Dual_Simplex_Example", LpMaximize)

# Create decision variables for the dual problem
y1 = LpVariable('y1', lowBound=0)  # y1 >= 0
y2 = LpVariable('y2', lowBound=0)  # y2 >= 0
y3 = LpVariable('y3', lowBound=0)  # y3 >= 0

# Objective function (minimization in dual corresponds to maximization here)
prob += 4 * y1 + 2 * y2 + 3 * y3, "Objective"

# Constraints for the dual problem
prob += y1 + y2 >= 3, "Constraint 1"
prob += y1 + y3 >= 2, "Constraint 2"

# Solve the problem using the dual simplex method
prob.solve()

# Print the status of the solution
print(f"Status: {LpStatus[prob.status]}")

# Print the results (optimal values for y1, y2, and y3)
print(f"y1 = {value(y1)}")
print(f"y2 = {value(y2)}")
print(f"y3 = {value(y3)}")

# Print the objective value (minimized value)
print(f"Optimal objective value: {value(prob.objective)}")

