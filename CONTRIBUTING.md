# Contributing guidelines

## Before contributing

Welcome to [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)! Before sending your pull requests, make sure that you **read the whole guidelines**. If you have any doubt on the contributing guide, please feel free to [state it clearly in an issue](https://github.com/TheAlgorithms/Python/issues/new) or ask the community in [Gitter](https://gitter.im/TheAlgorithms).

## Contributing

### Contributor

We are very happy that you consider implementing algorithms and data structure for others! This repository is referenced and used by learners from all over the globe. Being one of our contributors, you agree and confirm that:

- You did your work - no plagiarism allowed
  - Any plagiarized work will not be merged.
- Your work will be distributed under [MIT License](License) once your pull request is merged
- You submitted work fulfils or mostly fulfils our styles and standards

**New implementation** is welcome! For example, new solutions for a problem, different representations for a graph data structure or algorithm designs with different complexity.

**Improving comments** and **writing proper tests** are also highly welcome.

### Contribution

We appreciate any contribution, from fixing a grammar mistake in a comment to implementing complex algorithms. Please read this section if you are contributing your work.

#### Coding Style

We want your work to be readable by others; therefore, we encourage you to note the following:

- Please write in Python 3.x.

- If you know [PEP 8](https://www.python.org/dev/peps/pep-0008/) already, you will have no problem in coding style, though we do not follow it strictly. Read the remaining section and have fun coding!

- Always use 4 spaces to indent.

- Original code submission requires comments to describe your work.

- More on comments and docstrings:

  The following are considered to be bad and may be requested to be improved:

  ```python
  x = x + 2	# increased by 2
  ```

  This is too trivial. Comments are expected to be explanatory. For comments, you can write them above, on or below a line of code, as long as you are consistent within the same piece of code.

  *Sometimes, docstrings are avoided.* This will happen if you are using some editors and not careful with indentation:

  ```python
      """
  	This function sums a and b    
  """
  def sum(a, b):
      return a + b
  ```

  However, if you insist to use docstrings, we encourage you to put docstrings inside functions. Also, please pay attention to indentation to docstrings. The following is acceptable in this case:

  ```python
  def sumab(a, b):
      """
  	This function sums two integers a and b
  	Return: a + b
  	"""
      return a + b
  ```

- `lambda`, `map`, `filter`, `reduce` and complicated list comprehension are welcome and acceptable to demonstrate the power of Python, as long as they are simple enough to read.

  - This is arguable: **write comments** and assign appropriate variable names, so that the code is easy to read!

- Write tests to illustrate your work.

  The following "testing" approaches are **not** encouraged:

  ```python*
  input('Enter your input:') 
  # Or even worse...
  input = eval(raw_input("Enter your input: "))
  ```

  Please write down your test case, like the following:

  ```python
  def sumab(a, b):
      return a + b
  # Write tests this way:
  print(sumab(1,2))	# 1+2 = 3
  print(sumab(6,4))	# 6+4 = 10
  # Or this way:
  print("1 + 2 = ", sumab(1,2))	# 1+2 = 3
  print("6 + 4 = ", sumab(6,4))	# 6+4 = 10
  ```

- Avoid importing external libraries for basic algorithms. Use those libraries for complicated algorithms.

#### Other Standard While Submitting Your Work

- File extension for code should be `.py`. Jupiter notebook files are acceptable in machine learning algorithms.

- Strictly use snake case (underscore separated) in your file name, as it will be easy to parse in future using scripts.

  If possible, follow the standard *within* the folder you are submitting to.

- If you have modified/added code work, make sure the code compiles before submitting.

- If you have modified/added documentation work, make sure your language is concise and contains no grammar mistake.

- Add a corresponding explanation to [Algorithms-Explanation](https://github.com/TheAlgorithms/Algorithms-Explanation) (Optional but recommended).

- Most importantly,

  - **Be consistent with this guidelines while submitting.**
  - **Join** [Gitter](https://gitter.im/TheAlgorithms) **now!**
  - Happy coding!



Writer [@poyea](https://github.com/poyea), Jun 2019.
