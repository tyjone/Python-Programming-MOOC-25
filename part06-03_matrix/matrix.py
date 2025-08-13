def read_matrix():
    """Reads the matrix from matrix.txt and returns it as a list of lists of integers."""
    matrix = []
    with open("matrix.txt") as file:
        for line in file:
            row = [int(num) for num in line.strip().split(",")]
            matrix.append(row)
    return matrix

def matrix_sum():
    """Returns the sum of all elements in the matrix."""
    matrix = read_matrix()
    return sum(sum(row) for row in matrix)

def matrix_max():
    """Returns the maximum element in the matrix."""
    matrix = read_matrix()
    return max(max(row) for row in matrix)

def row_sums():
    """Returns a list of sums of each row in the matrix."""
    matrix = read_matrix()
    return [sum(row) for row in matrix]

