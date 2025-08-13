# Write your solution here
def print_letter_square(layers):
    size = 2 * layers - 1
    square = [['' for _ in range(size)] for _ in range(size)]

    for layer in range(layers):
        letter = chr(ord('A') + layers - layer - 1)
        for i in range(layer, size - layer):
            for j in range(layer, size - layer):
                square[i][j] = letter

    for row in square:
        print(''.join(row))


# Example usage
layers = int(input("Layers: "))
print_letter_square(layers)
