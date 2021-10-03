# This class represent a task
class Task:
    # Create a new task
    def __init__(self, tuple:()):
        
        # Set values for instance variables
        self.machine_id, self.processing_time = tuple
    # Sort
    def __lt__(self, other):
        return self.processing_time < other.processing_time
    # Print
    def __repr__(self):
        return ('(Machine: {0}, Time: {1})'.format(self.machine_id, self.processing_time))
# This class represent an assignment
class Assignment:
    # Create a new assignment
    def __init__(self, job_id:int, task_id:int, start_time:int, end_time:int):
        # Set values for instance variables
        self.job_id = job_id
        self.task_id = task_id
        self.start_time = start_time
        self.end_time = end_time
    # Print
    def __repr__(self):
        return ('(Job: {0}, Task: {1}, Start: {2}, End: {3})'.format(self.job_id, self.task_id, self.start_time, self.end_time))    
# This class represents a schedule
class Schedule:
    # Create a new schedule
    def __init__(self, jobs:[]):
        
        # Set values for instance variables
        self.jobs = jobs
        self.tasks = {}
        for i in range(len(self.jobs)):
            for j in range(len(self.jobs[i])):
                self.tasks[(i, j)] = Task(self.jobs[i][j])
        self.assignments = {}
    # Get the next assignment
    def backtracking_search(self) -> bool:
        # Prefer tasks with an early end time
        best_task_key = None
        best_machine_id = None
        best_assignment = None
        # Loop all tasks
        for key, task in self.tasks.items():
            # Get task variables
            job_id, task_id = key
            machine_id = task.machine_id
            processing_time = task.processing_time
            # Check if the task needs a predecessor, find it if needs it
            predecessor = None if task_id > 0 else Assignment(0, 0, 0, 0)
            if (task_id > 0):
                # Loop assignments
                for machine, machine_tasks in self.assignments.items():
                    # Break out from the loop if a predecessor has been found
                    if(predecessor != None):
                        break
                    # Loop machine tasks
                    for t in machine_tasks:
                        # Check if a predecessor exsits
                        if(t.job_id == job_id and t.task_id == (task_id - 1)):
                            predecessor = t
                            break
            # Continue if the task needs a predecessor and if it could not be found
            if(predecessor == None):
                continue
            # Get an assignment
            assignment = self.assignments.get(machine_id)
            # Calculate the end time
            end_time = processing_time
            if(assignment != None):
                end_time += max(predecessor.end_time, assignment[-1].end_time)
            else:
                end_time += predecessor.end_time
            # Check if we should update the best assignment
            if(best_assignment == None or end_time < best_assignment.end_time):
                best_task_key = key
                best_machine_id = machine_id
                best_assignment = Assignment(job_id, task_id, end_time - processing_time, end_time)
        # Return failure if we can not find an assignment (Problem not solvable)
        if(best_assignment == None):
            return False
        # Add the best assignment
        assignment = self.assignments.get(best_machine_id)
        if(assignment == None):
            self.assignments[best_machine_id] = [best_assignment]
        else:
            assignment.append(best_assignment)
        # Remove the task
        del self.tasks[best_task_key]
        # Check if we are done
        if(len(self.tasks) <= 0):
            return True
        # Backtrack
        self.backtracking_search()
# The main entry point for this module
def main():
    # Input data: Task = (machine_id, time)
    jobs = [[(0, 3), (1, 2), (2, 2)], # Job 0
            [(0, 2), (2, 1), (1, 4)], # Job 1
            [(1, 4), (2, 3)]] # Job 2
    
    # Create a schedule
    schedule = Schedule(jobs)
    # Find a solution
    schedule.backtracking_search()
    # Print the solution
    print('Final solution:')
    for key, value in sorted(schedule.assignments.items()):
        print(key, value)
    print()
    
# Tell python to run main method
if __name__ == "__main__": main()
