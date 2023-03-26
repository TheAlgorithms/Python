# Project Euler

Problems are taken from https://projecteuler.net/, the Project Euler. [Problems are licensed under CC BY-NC-SA 4.0](https://projecteuler.net/copyright).

Project Euler is a series of challenging mathematical/computer programming problems that require more than just mathematical
insights to solve. Project Euler is ideal for mathematicians who are learning to code.

The solutions will be checked by our [automated testing on GitHub Actions](https://github.com/TheAlgorithms/Python/actions) with the help of [this script](https://github.com/TheAlgorithms/Python/blob/master/scripts/validate_solutions.py). The efficiency of your code is also checked. You can view the top 10 slowest solutions on GitHub Actions logs (under `slowest 10 durations`) and open a pull request to improve those solutions.


## Solution Guidelines

Welcome to [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)! Before reading the solution guidelines, make sure you read the whole [Contributing Guidelines](https://github.com/TheAlgorithms/Python/blob/master/CONTRIBUTING.md) as it won't be repeated in here. If you have any doubt on the guidelines, please feel free to [state it clearly in an issue](https://github.com/TheAlgorithms/Python/issues/new) or ask the community in [Gitter](https://app.gitter.im/#/room/#TheAlgorithms_community:gitter.im). You can use the [template](https://github.com/TheAlgorithms/Python/blob/master/project_euler/README.md#solution-template) we have provided below as your starting point but be sure to read the [Coding Style](https://github.com/TheAlgorithms/Python/blob/master/project_euler/README.md#coding-style) part first.

### Coding Style

* Please maintain consistency in project directory and solution file names. Keep the following points in mind:
  * Create a new directory only for the problems which do not exist yet.
  * If you create a new directory, please create an empty `__init__.py` file inside it as well.
  * Please name the project **directory** as `problem_<problem_number>` where `problem_number` should be filled with 0s so as to occupy 3 digits. Example: `problem_001`, `problem_002`, `problem_067`, `problem_145`, and so on.

* Please provide a link to the problem and other references, if used, in the **module-level docstring**.

* All imports should come ***after*** the module-level docstring.

* You can have as many helper functions as you want but there should be one main function called `solution` which should satisfy the conditions as stated below:
  * It should contain positional argument(s) whose default value is the question input. Example: Please take a look at [Problem 1](https://projecteuler.net/problem=1) where the question is to *Find the sum of all the multiples of 3 or 5 below 1000.* In this case the main solution function will be `solution(limit: int = 1000)`.
  * When the `solution` function is called without any arguments like so: `solution()`, it should return the answer to the problem.

* Every function, which includes all the helper functions, if any, and the main solution function, should have `doctest` in the function docstring along with a brief statement mentioning what the function is about.
  * There should not be a `doctest` for testing the answer as that is done by our GitHub Actions build using this [script](https://github.com/TheAlgorithms/Python/blob/master/scripts/validate_solutions.py). Keeping in mind the above example of [Problem 1](https://projecteuler.net/problem=1):

  ```python
  def solution(limit: int = 1000):
      """
      A brief statement mentioning what the function is about.

      You can have a detailed explanation about the solution method in the
      module-level docstring.

      >>> solution(1)
      ...
      >>> solution(16)
      ...
      >>> solution(100)
      ...
      """
    ```

### Solution Template

You can use the below template as your starting point but please read the [Coding Style](https://github.com/TheAlgorithms/Python/blob/master/project_euler/README.md#coding-style) first to understand how the template works.

Please change the name of the helper functions accordingly, change the parameter names with a descriptive one, replace the content within `[square brackets]` (including the brackets) with the appropriate content.

```python
"""
Project Euler Problem [problem number]: [link to the original problem]

... [Entire problem statement] ...

... [Solution explanation - Optional] ...

References [Optional]:
- [Wikipedia link to the topic]
- [Stackoverflow link]
...

"""
import module1
import module2
...

def helper1(arg1: [type hint], arg2: [type hint], ...) -> [Return type hint]:
    """
    A brief statement explaining what the function is about.

    ... A more elaborate description ... [Optional]

    ...
    [Doctest]
    ...

    """
    ...
    # calculations
    ...

    return


# You can have multiple helper functions but the solution function should be
# after all the helper functions ...


def solution(arg1: [type hint], arg2: [type hint], ...) -> [Return type hint]:
    """
    A brief statement mentioning what the function is about.

    You can have a detailed explanation about the solution in the
    module-level docstring.

    ...
    [Doctest as mentioned above]
    ...

    """

    ...
    # calculations
    ...

    return answer


if __name__ == "__main__":
    print(f"{solution() = }")
```
