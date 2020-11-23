class Matrix:
    def __init__(self, matrix):
        self.list = matrix

    def __str__(self):
        val_str = ""
        for i in self.list:
            val_str = val_str + (" ".join(str(x) for x in i))
            val_str = val_str + "\n"
        return val_str

    def __add__(self, other):
        new_matrix = []
        for x in range(len(self.list)):
            add_matrix = []
            for y in range(len(self.list[x])):
                add_matrix.append(self.list[x][y] + other.list[x][y])
            new_matrix.append(add_matrix)
        return Matrix(new_matrix)


matrix1 = Matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
matrix2 = Matrix([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
matrix3 = matrix1 + matrix2
print(matrix3)
