from .stack import Stack

__author__ = "Dhyey Thakkar"

def balanced_brackets(brackets):
  """
  >>>Use a Stack to check if the given string of brackets is balanced or not 
     P.S it is updated part of balanced_parentheses.In this you can use "[{(<>)}]"
  >>>	balanced_brackets("{{[]}}()(<>)")
      returns True
  
  >>> balanced_brackets("[{]()<>")
      retruns False
	
  
  """
  brackets_stack = Stack(len(brackets))
  for bracket in brackets:
    if bracket in "{[(<":
      bracket_stack.push(bracket)
    elif bracket in ">]})":
      if bracket_stack.is_empty() or bracket_stack.peek() != bracket:
        return False
      bracket_stack.pop()
  return bracket_stack.is_empty()

if __name__ == "__main__":
    test_cases = ["[{[]}()<()>]", "[{}<(>]", "[[[{}]<>]()]"]
    print("Balanced brackets demonstration:\n")
    for test_case in test_cases:
        print(test_case + ": " + str(balanced_brackets(test_case)))



  
