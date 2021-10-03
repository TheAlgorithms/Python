def validateBST(tree):
  
  def validateBstHelper(tree, minimum, maximum):
    if tree is None:
        return True
    
    if tree.value < minimum or tree.value > maximum:
        return False
    leftIsValid = validateBstHelper(tree.left, minimum, tree.value)
    rightIsValid = validateBstHelper(tree.right, tree.value, maximum)
    
    return leftIsValid and rightIsValid
  
  return validateBstHelper(tree, float("-inf"), float("inf"))
