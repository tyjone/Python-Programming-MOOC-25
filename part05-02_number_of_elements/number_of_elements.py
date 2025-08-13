# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    element_num = 0
    for x in range(len(my_matrix)):
        for y in range(len(my_matrix[x])):
            print(f"Row: {my_matrix[x]} | Collumn: {my_matrix[x][y]}")
            if my_matrix[x][y] == element:
                element_num += 1
    return element_num

        
if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
            