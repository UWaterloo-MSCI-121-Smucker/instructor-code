"""
A file named data.txt contains in it a 3x5 (3 rows, 5 columns) matrix.
Each line of the file contains one number.  The data is "by rows", which
means that the first 5 numbers are the first row, and the next 5 are the 
next row, etc.  We want to write code to read this data into our program.
"""

def read_matrix( nrows, ncols, filename):
    """Reads a by_rows matrix from the file where each element is on a line by itself."""
    matrix = list()
    infile = open( filename, "r")

    i = 0
    while i < nrows:
        row = list()
        matrix.append( row )
        j = 0
        while j < ncols:
            value = float( infile.readline().strip() )
            row.append( value )
            j = j + 1
        i = i + 1

    infile.close()
    return matrix

def read_matrix_v2( nrows, ncols, filename):
    """Reads a by_rows matrix from the file where each element is on a line by itself."""
    matrix = list()
    with open( filename, "r") as infile:
        for i in range(nrows):
            row = list()
            matrix.append( row )
            for j in range(ncols):
                row.append( float(infile.readline().strip()) )
    return matrix

def print_matrix( matrix ):
    i = 0 
    while i < len(matrix):        
        j = 0 
        while j < len(matrix[i]):
            print( matrix[i][j], end='')
            if j < len(matrix[i])-1:
                print( ", ", end='')
            j = j + 1
        print()
        i = i + 1


def main():
    """Demo the code."""
    filename = "data.txt"
    nrows = 3
    ncolumns = 5
    #matrix = read_matrix( nrows, ncolumns, filename )
    matrix = read_matrix_v2( nrows, ncolumns, filename )
    print(matrix)
    print_matrix( matrix )


if __name__ == "__main__":
    main()