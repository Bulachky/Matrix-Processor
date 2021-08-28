class Matrix:
    def __init__(self, rows, columns, matrix):
        self.rows = rows
        self.columns = columns
        self.matrix = matrix

    def matrix_sum(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            print('The operation cannot be performed.')
        elif self.rows == other.rows and self.columns == other.columns:
            sum_mat = [[str(in_or_fl(self.matrix[i][j]) + in_or_fl(other.matrix[i][j])) for j in range(self.columns)] for i in range(self.rows)]
            print_mat(sum_mat)

    def scalar_mul(self, scalar):
        scalar_mat = [[str(in_or_fl(self.matrix[i][j]) * scalar) for j in range(self.columns)] for i in range(self.rows)]
        print_mat(scalar_mat)

    def matrix_mul(self, other):
        if self.columns == other.rows:
            prod_mat = []
            for i in range(self.rows):
                prod_mat.append([])
                for j in range(other.columns):
                    dot_product = str(sum([(in_or_fl(self.matrix[i][x]) * in_or_fl(other.matrix[x][j])) for x in range(other.rows)]))
                    prod_mat[i].append(dot_product)
            print_mat(prod_mat)
        else:
            print('The operation cannot be performed.')

    def main_trans(self):
        return [[self.matrix[j][i] for j in range(self.columns)] for i in range(self.rows)]

    def vertical_trans(self):
        return [self.matrix[i][::-1] for i in range(self.rows)]

    def horizontal_trans(self):
        return self.matrix[::-1]

    def side_trans(self):
        return [[self.matrix[j][i] for j in range(self.columns)][::-1] for i in range(self.rows)][::-1]

    def determined(self):
        solution = 0
        if self.rows == 1:
            return in_or_fl(self.matrix[0])
        elif self.rows != self.columns:
            print("Can't calculate determined, not squared matrix.")
        elif self.rows == 2 and self.columns == 2:
            return in_or_fl(self.matrix[0][0]) * in_or_fl(self.matrix[1][1]) - in_or_fl(self.matrix[0][1]) * in_or_fl(self.matrix[1][0])
        else:
            for j in range(self.columns):
                element = in_or_fl(self.matrix[0][j]) * (-1) ** j  # j is column
                new_mat = [row[:] for row in self.matrix]
                new_mat = new_mat[1:]
                for row in range(len(new_mat)):
                    del new_mat[row][j]
                new_mat = Matrix(len(new_mat), len(new_mat[0]), new_mat)
                solution += element * new_mat.determined()
            return solution

    def find_cofactors(self):  # cofactor[i][j] = minor * (-1) ^ (i+j)
        cofactors_mat = []
        for i in range(self.rows):
            cofactors_mat.append([])
            for j in range(self.columns):
                new_mat = [row[:] for row in self.matrix]
                del new_mat[i]
                for row in range(len(new_mat)):
                    del new_mat[row][j]
                print()
                new_mat = Matrix(len(new_mat), len(new_mat[0]), new_mat)
                cofactor = (-1) ** (i + j) * new_mat.determined()
                cofactors_mat[i].append(cofactor)
        return cofactors_mat

    def inverse_mat(self):
        det = self.determined()
        if det == 0:
            print("This matrix doesn't have an inverse.")
        else:
            scalar = 1 / det
            cofactors_mat = Matrix(self.rows, self.columns, self.find_cofactors())
            transpose_mat = Matrix(self.rows, self.columns, cofactors_mat.main_trans())
            transpose_mat.scalar_mul(scalar)


def matrix_transposition():
    print('\n1. Main diagonal')
    print('2. Side diagonal')
    print('3. Vertical line')
    print('4. Horizontal line')
    choice_t = int(input('Your choice (please enter integer):',))
    rows, columns = take_dim()
    matrix = Matrix(rows, columns, take_mat(rows, columns))
    if choice_t == 1:
        print_mat(matrix.main_trans())
    elif choice_t == 2:
        print_mat(matrix.side_trans())
    elif choice_t == 3:
        print_mat(matrix.vertical_trans())
    elif choice_t == 4:
        print_mat(matrix.horizontal_trans())
    else:
        print('Invalid input, please try again.')


def in_or_fl(number):
    number = float(number)
    if number % 1 == 0:
        return int(number)
    return number


def print_mat(matrix):
    print('The result is:')
    for row in matrix:
        print(' '.join(row))
    print()


def take_dim(number=''):
    rows, columns = map(int, input(f'Enter size of {number}matrix:',).split())
    return rows, columns  # [0] = rows , [1] = columns


def take_mat(rows, columns, number=''):
    print(f'Enter {number}matrix:')
    if rows == 1 and columns == 1:
        return [input()]
    return [input().split() for _ in range(rows)]


def take_scalar():
    return in_or_fl(input('Enter constant:'))


def options():
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')
    return int(input('Your choice (please enter integer):',))


while True:
    choice = options()
    if choice == 1:
        rows_a, columns_a = take_dim('First ')
        mat_a = Matrix(rows_a, columns_a, take_mat(rows_a, columns_a, 'First '))
        rows_b, columns_b = take_dim('second ')
        mat_b = Matrix(rows_b, columns_b, take_mat(rows_b, columns_b, 'second '))
        mat_a.matrix_sum(mat_b)
    elif choice == 2:
        rows_a, columns_a = take_dim()
        mat = Matrix(rows_a, columns_a, take_mat(rows_a, columns_a))
        mat.scalar_mul(take_scalar())
    elif choice == 3:
        rows_a, columns_a = take_dim('First ')
        mat_a = Matrix(rows_a, columns_a, take_mat(rows_a, columns_a, 'First '))
        rows_b, columns_b = take_dim('second ')
        mat_b = Matrix(rows_b, columns_b, take_mat(rows_b, columns_b, 'second '))
        mat_a.matrix_mul(mat_b)
    elif choice == 4:
        matrix_transposition()
    elif choice == 5:
        rows_a, columns_a = take_dim()
        mat = Matrix(rows_a, columns_a, take_mat(rows_a, columns_a))
        print(f'The Result is:\n{mat.determined()}\n')
    elif choice == 6:
        rows_a, columns_a = take_dim()
        mat = Matrix(rows_a, columns_a, take_mat(rows_a, columns_a))
        mat.inverse_mat()
    elif choice == 0:
        break
    else:
        print('Please enter a valid integer.')
        continue
