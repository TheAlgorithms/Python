from .stack import Stack

__author__ = "Dhyey Thakkar"

def balanced_brackets(brackets):
  """
  >>>Use a Stack to check if the given string of brackets is balanced or not
  
  """
  brackets_stack = Stack(len(brackets))
  for bracket in brackets:
    if bracket in "{[(":
      bracket_stack.push(bracket)
  
