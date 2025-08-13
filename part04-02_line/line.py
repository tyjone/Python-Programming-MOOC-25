# Write your solution here
def line(length, char_string):
    if char_string:
        char = char_string[0]
    else:
        char = '*'
    print(char * length)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")