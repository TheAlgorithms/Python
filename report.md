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

Plan for refactoring complex code:

Estimated impact of refactoring (lower CC, but other drawbacks?).

Carried out refactoring (optional, P+):

git diff ...

## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.

How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

We used the (coverage)[https://coverage.readthedocs.io/en/7.1.0/] tool to measure branch coverage. It was really easy to use and well documented. Our project used both `pytest`, `doctest` and `unittest` python test frameworks, but the coverage tool integrated fine with them all.

The installation was a simple `pip` call, and measuring coverage was as simple as replacing `python3 -m uniitest file.py` with `coverage run -m uniitest file.py`

Overall, a pleasant experience!

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
- `_remove_repair@red_black_tree.py` : 0% (no tests) # py -m doctest d/d/rbt.py 
- `canny@canny.py` : 84% # `coverage run --branch -m pytest digital_image_processing/test_digital_image_processing.py`
- `points_to_polynomial@polynom_for_points` : 82% # doctest, single function
- `search@a_star.py` : 0% (no tests)
- `bidirectional_dij@bi_directional_djikstra` : 89% # coverage run -m doctest graphs/bi_directional_dijkstra.py 
- `inverse_of_matrix@inverse_of_matrix.py` : 100% (skipping)
- `solution@problem_049/sol1.py` : 98%
- `problem_551/sol1.py` : 98%
- `conway_game_of_life` : 72%
- `

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
