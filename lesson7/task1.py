class Matrix ():
    def __init__ (self, matrix):
        self.matrix = matrix 
    def __repr__ (self):
        return '\n'.join (','.join (str (m) for m in n) for n in self.matrix)
    def __add__(self, other):
        return Matrix(list(map(
                        lambda x, y: list(map(lambda z, w: z + w, x, y)),
                        self.matrix, other.matrix)))

list_matrix_01 = [[1, 2, 3], [3, 3, 3], [4, 3, 2]]
list_matrix_02 = [[2, 5, 5], [4, 3, 3], [1, 1, 2]]
matr01 = Matrix(list_matrix_01)
matr02 = Matrix(list_matrix_02)
matr03 = matrix01 + matrix02

print(matr01, end='\n\n')
print(matr02, end='\n\n')
print(matr03)