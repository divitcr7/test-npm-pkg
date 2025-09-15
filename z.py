def matrix_operations():
    """Demonstrate some matrix operations."""
    # Create random 3x3 matrix
    matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
    
    print("Random 3x3 Matrix:")
    for row in matrix:
        print(row)
    
    # Calculate determinant (for 3x3 matrix)
    def determinant_3x3(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
                m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
                m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    
    det = determinant_3x3(matrix)
    print(f"Determinant: {det}")
    
    # Transpose matrix
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("Transpose:")
    for row in transpose:
        print(row)

def recursive_factorial(n: int) -> int:
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)

def binary_search(arr: List[int], target: int) -> int:
    """Perform binary search on a sorted array."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1