"""
This is a pure Python implementation for Job Sequencing Problem
reference: https://www.geeksforgeeks.org/job-sequencing-problem/
For doctests run following command:
python3 -m doctest -v job_sequencing_problem.py
Objective
Given some jobs along with their deadline and profit.
We need to find maximum profit if all jobs takes unit time to complete
Approach
Sort all jobs in decreasing order of profit. 
Iterate on jobs in decreasing order of profit.For each job , do the following : 
Find a time slot i, such that slot is empty and i < deadline and i is greatest.Put the job in 
this slot and mark this slot filled. 
If no such i exists, then ignore the job. 
"""

def print_job_scheduling(Jobs : x, MaxDeadline:t) -> List:
  """Function to print all jobs which can be completed
    Args:
        Jobs [list]: A list of all jobs along with deadline and profits
        MaxDeadline [int]: Maximum deadline among all the jobs
    Returns:
        job [list]: Jobs that can be completed
    Examples:
    >>> print_job_scheduling [[1, 2, 100],
           [2, 1, 19],
           [3, 2, 27],
           [4, 1, 25],
           [5, 3, 15]])
    [2,-1,1,-1,3]
    """
    n = len(x)
 
    for i in range(n):
        for j in range(n - 1 - i):
            if x[j][2] < x[j + 1][2]:
                x[j], x[j + 1] = x[j + 1], x[j]
 
    result = [False] * t
 
    job = ['-1'] * t
 
    for i in range(len(arr)):
 
        for j in range(min(t - 1, x[i][1] - 1), -1, -1):
 
            if result[j] is False:
                result[j] = True
                job[j] = x[i][0]
                break
    return job
 
if __name__ == "__main__":
    import doctest

    doctest.testmod()
