def find_longest_path_from_a_cell(i: int, j: int, mat: 'list[list[int]]', dp: 'list[list[int]]') -> int:
  """
  Find the length of longest path of increasing sequence in a matrix 
  from cell at (i,j) in matrix mat, 
  dp has the longest path from any cell (x,y), or else, -1.
  >>> find_longest_path_from_a_cell(0, 0, [[0, 1], [3, 2]], [[-1, -1], [-1, -1]])
  4
  """
  n = len(mat)
  if (i<0 or i>= n or j<0 or j>= n):
    return 0
  if (dp[i][j] != -1):
    return dp[i][j]

  x, y, z, w = -1, -1, -1, -1

  if (j<n-1 and ((mat[i][j] +1) == mat[i][j + 1])):
    x = 1 + find_longest_path_from_a_cell(i, j + 1, mat, dp)
  if (j>0 and (mat[i][j] +1 == mat[i][j-1])):
    y = 1 + find_longest_path_from_a_cell(i, j-1, mat, dp)
  if (i>0 and (mat[i][j] +1 == mat[i-1][j])):
    z = 1 + find_longest_path_from_a_cell(i-1, j, mat, dp)
  if (i<n-1 and (mat[i][j] +1 == mat[i + 1][j])):
    w = 1 + find_longest_path_from_a_cell(i + 1, j, mat, dp)

  dp[i][j] = max(x, max(y, max(z, max(w, 1))))
  return dp[i][j]

def find_longest_path_in_a_matrix(mat: 'list[list[int]]') -> int:
  """
  Find the length of longest path of increasing sequence in a matrix mat.
  >>> find_longest_path_in_a_matrix([[0, 1], [3, 2]])
  4
  """
  n = len(mat)
  result = 1
  dp =[[-1 for i in range(n)]for i in range(n)]
  for i in range(n):
    for j in range(n):
      if (dp[i][j] == -1):
        find_longest_path_from_a_cell(i, j, mat, dp)
      result = max(result, dp[i][j]);
  return result

if __name__ == "__main__":
  import doctest
  doctest.testmod()
