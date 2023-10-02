# Напишите функцию для транспонирования матрицы

def transpose(matrix):
  """ Принимает матрицу в виде списка списков. 
  Возвращает транспонированную матрицу."""
  rows = len(matrix) 
  columns = len(matrix[0])
  
  transposed_matrix = []
  for i in range(rows):
      transposed_matrix.append([0] * columns)

  for i in range(rows):
    for j in range(columns):
     transposed_matrix[j][i] = matrix[i][j]

  return transposed_matrix

matrix =  [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
print(transpose(matrix))
#print(help(transpose))
