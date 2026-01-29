"""
Search 2D Matrix..
You are given an m x n integer matrix matrix with the following two properties:
* Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
* Given an integer target, return true if target is in matrix or false otherwise.
"""


def searchMatrix(matrix, target: int) -> bool:
  if not matrix or not matrix[0]:
    return False

  rows,cols = len(matrix),len(matrix[0])
  left,right = 0, rows*cols - 1

  while left<= right:
    mid = (left+right) // 2
    new_row, new_col = mid//cols , mid%cols
    if matrix[new_row][new_col] == target:
      print(f"Target {target} found at row {new_row} and column {new_col}")
      return True
    elif matrix[new_row][new_col] < target:
      left = mid + 1
    else:
      right = mid - 1
  return False


searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=13)

searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)