# Copy here code of line function from previous exercise and use it in your solution
def line(length, char_string):
    if char_string:
        char = char_string[0]
    else:
        char = '*'
    squares = char * length
    print(squares)

def shape(size1,length1,size2,length2):
    for i in range(size1 + 1):
        line(i, length1)
    for i in range(size2):
        line(size1, length2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")