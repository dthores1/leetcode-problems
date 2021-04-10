"""
    Given a matrix of m * n elements (m rows, n columns), return all elements 
    of the matrix in spiral order.

    Example:

        Input:
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
        Output:
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
"""
def spiralMatrix(matrix):
    result = []
    visited = [[False for row in matrix] for col in matrix[0]]
    search(matrix, visited, 0, 0, result)
    return result

def search(matrix, visited, row, col, result):
    if visited[row][col] == False:
        result.append(matrix[row][col])
        visited[row][col] = True

    for cell in get_next(row, col, matrix, visited):
        row, col = cell
        search(matrix, visited, row, col, result)

def get_next(row, col, matrix, visited):
    neighbors = []
    if col < len(matrix)-1 and visited[row][col+1] == False:
        neighbors.append([row, col+1])    
    if row < len(matrix[0])-1 and visited[row+1][col] == False:
        neighbors.append([row+1, col])
    if col > 0 and visited[row][col-1] == False:
        neighbors.append([row, col-1])        
    if row > 0 and visited[row-1][col] == False:
        neighbors.append([row-1, col])

    return neighbors

matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(spiralMatrix(matrix))
