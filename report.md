# Report for assignment 3

## Project

Name: TheAlgorithm/Python

URL: **[GitHub - TheAlgorithms/Python: All Algorithms implemented in Python](https://github.com/TheAlgorithms/Python)**

Description: The project contains algorithms implemented in Python that can be used for learning purposes.

## Onboarding experience

Did it build and run as documented?

See the assignment for details; if everything works out of the box,
there is no need to write much here. If the first project(s) you picked
ended up being unsuitable, you can describe the "onboarding experience"
for each project, along with reason(s) why you changed to a different one.

## Complexity

1. What are your results for ten complex functions?
   * Did all methods (tools vs. manual count) get the same result?
   * Are the results clear?
2. Are the functions just complex, or also long?
3. What is the purpose of the functions?
4. Are exceptions taken into account in the given measurements?
5. Is the documentation clear w.r.t. all the possible outcomes?

## Refactoring

We made plans for refactoring those 5 complex functions:

1. `_remove_repair@212-283@.\data_structures\binary_tree\red_black_tree.py`:

   We know that maintaining the structure of a red black tree after deleting a node is very complicated because there are many cases to be considered. In the original _remove_repair functions, authors write those conditions in a single function using 8 if statements. Therefore, it’s possible to divide them into 8 small functions.

   We managed to refactor this function by splitting it into many small and easy-to-understand functions. The maximum cyclomatic complexity of all relevant functions reduces to 6 using Lizard. The previous CC of _remove_repair function was 31, so there’s about a 81% reduction in CC after refactor.

2. `canny@21-113@.\digital_image_processing\edge_detection\canny.py`:

	Theoretically, canny algorithm can be divided into 5 major steps:	
      1. Apply Gaussian kernel to remove the noise in the image.
      2. Find the gradient of the image.
      3. Use non-maximum suppression on gradient magnitude in gradient direction.
      4. Use double thresholding to pick out potential edges.
      5. Track edges by suppressing weak edges that are not connected to strong edges.

	Currently, the canny function consists of those steps altogether. There are no independent functions implementing steps 1-5. Therefore, we can just write a function for each of those steps.
   
   Besides, it’s worth noticing that in step 3, we need to consider the gradient magnitude in four directions: horizontally, sub-diagonally, vertically, diagonally. Therefore, we can write four functions for each of those 4 cases, which further reduces cyclomatic complexity.

   We managed to refactor this function by splitting it into many small and easy-to-understand functions. The maximum cyclomatic complexity of all relevant functions reduces to 6 using Lizard. The previous CC of canny function was 26, so there’s about a 77% reduction in CC after refactor.

3. `points_to_polynomial@1-103@.\linear_algebra\src\polynom_for_points.py`:

	This function consists of following major steps:
      1. Error handling: check if the input is illegal, e.g., empty input or wrong dimension.
      2. Feature matrix generation: generate feature matrix based on data points.
      3. Dependent values extraction: generate dependent value vector: y coordinates of data points.
      4. Solution finding: find coefficients of the polynomial using Gaussian Elimination technique.
      5. Solution string generation: stringfy the output polynomial so it can be printed.
	The function can be divided into those 5 smaller functions.
	
   We managed to refactor this function by splitting it into many small and easy-to-understand functions. The maximum cyclomatic complexity of all relevant functions reduces to 7 using Lizard. The previous CC of points_to_polynomial function was 21, so there’s about a 67% reduction in CC after refactor.

4. `search@12-74@.\graphs\a_star.py`: 
	
   At each step, A* algorithm selects the node with the lowest evaluation function value from the priority queue and adds it to the visited list. The algorithm then examines the neighbors of the selected node, and for each neighbor that has not been visited, it calculates a new evaluation function value based on the cost to reach that neighbor and the estimated distance to the goal node. If the neighbor is not in the priority queue, it is added to the queue with its new evaluation function value. If the neighbor is already in the priority queue, the algorithm updates its evaluation function value if the new value is lower than the current value.

   The step above, which I called "expand" because it is expanding the searching tree, accounts for a significant portion of the total complexity. Therefore, we decided to write a single function for it.

   Beside, at the very end of the A* algorithm, the path should be printed based on the previous action history. We moved it out of the original search function and wrote a function for it.
	
   We managed to refactor this function by splitting it into many small and easy-to-understand functions. The maximum cyclomatic complexity of all relevant functions reduces to 8 using Lizard. The previous CC of search function was 20, so there’s about a 60% reduction in CC after refactor.

5. `bidirectional_dij@20-107@.\graphs\bi_directional_dijkstra.py`:
	
   For bi-directional Dijkstra’s algorithm, we need to prepare for 2 priority queues for forward pass and backward pass. And for both of them, we need to update the shortest distance and relaxation. Therefore, it’s a straightforward idea to write those methods in separate functions.

   First, we moved part of the code that pops the node from the priority queue and marks it as visited to the add_visited function. Then, we moved part of the code that does relaxation to the forward_pass and backward_pass function.
	
   We managed to refactor this function by splitting it into many small and easy-to-understand functions. The maximum cyclomatic complexity of all relevant functions reduces to 8 using Lizard. The previous CC of bi_directional_dij function was 20, so there’s about a 60% reduction in CC after refactor.

## Coverage

### Tools

For Python, there’s a good code coverage tool called `coverage.py`, which is user-friendly. It can be installed by `pip install coverage`.

To investigate the coverage in a particular Python file, using `coverage run --branch {py. filepath}` Then you can check the result by either `coverage report` to generate a standard output on your terminal, or `coverage html` to generate a detailed html file, which gives a visualized result.

Besides, `coverage` supports `pytest` well. To investigate how much code is covered by unit tests written in `pytest` rather than `main` function, using `coverage run --branch -m pytest {py. Filepath}`, which will only run the unit tests and check the test coverage.

The documentation is well organized and easy to understand. It can be found on https://coverage.readthedocs.io/en/7.1.0/.

### Automated coverage tool
`coverage` helps us find the branch coverage of the five functions with high cyclomatic complexity. However, before we get the result, we should manually identify how many branches the function has in total. Then we check the result generated by `coverage` and confirm how many of them are missing.

1. `_remove_repair@212-283@.\data_structures\binary_tree\red_black_tree.py` CCN: 31, coverage: 15/22 for main, 15/22 for test.
2. `canny@21-113@.\digital_image_processing\edge_detection\canny.py` CCN: 26, coverage: 18/22 for main.
3. `points_to_polynomial@1-103@.\linear_algebra\src\polynom_for_points.py` CCN: 21, coverage: 26/30 for main.
4. `search@12-74@.\graphs\a_star.py` CCN: 20, coverage: 11/12 for main.
5. `bidirectional_dij@20-107@.\graphs\bi_directional_dijkstra.py` CCN: 20 coverage: 27/32 for main.



We used the (coverage)[https://coverage.readthedocs.io/en/7.1.0/] tool to measure branch coverage. It was really easy to use and well documented. Our project used both `pytest`, `doctest` and `unittest` python test frameworks, but the coverage tool integrated fine with them all.

The installation was a simple `pip` call, and measuring coverage was as simple as replacing `python3 -m uniitest file.py` with `coverage run -m uniitest file.py`

However, as the project used tests a bit differently between files, some with doctests on a function basis and some with separate `test_` files, a bit of tinkering was required to test the branch coverage for the selected functions. A separate test runner script was created to extract only our wanted results, see `specific_tests.py`.


### Your own coverage tool

Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

### Evaluation

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

## Coverage improvement

Show the comments that describe the requirements for the coverage.

Report of old coverage:

function@file                                                   Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------------------------------
`bidirectional_dij@graphs/bi_directional_dijkstra.py`           65     58     38      1     8%
`new_generation@cellular_automata/conways_game_of_life.py`      47     20     30      0    64%
`points_to_polynomial@linear_algebra/src/polynom_for_points.py` 68     16     38      4    79%
`canny@digital_image_processing/edge_detection/canny.py`        60      9     34      2    84%
`solution@project_euler/problem_049/sol1.py`                    57      8     50      1    90%
`inverse_of_matrix@matrix/inverse_of_matrix.py`                 37      4     20      0    93%

(missing tests:)
`_remove_repair@data_structures/binary_tree/red_black_tree.py`
`remove@data_structures/binary_tree/red_black_tree.py`
`search@graphs/a_star.py
`next_term@project_euler/problem_551/sol1.py`
-------------------------------------------------------------------------------------------------
TOTAL                                                           334    115    210      8    68%



Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

## Self-assessment: Way of working

Current state according to the Essence standard: ...

Was the self-assessment unanimous? Any doubts about certain items?

How have you improved so far?

Where is potential for improvement?

## Overall experience

What are your main take-aways from this project? What did you learn?

Is there something special you want to mention here?
