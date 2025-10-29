def create_matrix(num_rows, num_cols):
    rows = [None] * num_rows
    for i in range(num_rows):
        rows[i] = [0.0] * num_cols
    return rows


def build_identity_matrix(n):
    """Returns an identity matrix as a list of lists (float) of size n."""
    matrix = list()
    for i in range(n):
        row = list()
        matrix.append(row)
        for j in range(n):
            if i == j:
                row.append(1.0)
            else:
                row.append(0.0)
    return matrix


def print_matrix( matrix ):
    """Prints out a matrix that is represented as a list of lists (float)."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end="")
            if j != len(matrix[i])-1:
                print(" ",end="")
        print()

print_matrix(build_identity_matrix(3))
print()

my_matrix = create_matrix(num_rows=2,num_cols=3)
print_matrix(my_matrix)