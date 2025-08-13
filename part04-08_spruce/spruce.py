# Write your solution here
def spruce(size):
    print("a spruce!")
    for i in range(1, size + 1):
        stars = 2 * i - 1
        spaces = size - i
        print(" " * spaces + "*" * stars)
    print(" " * (size - 1) + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)