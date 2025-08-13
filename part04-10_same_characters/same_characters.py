# Write your solution here
def same_chars(s, i, j):
    # Check if both indexes are within the bounds of the string
    if 0 <= i < len(s) and 0 <= j < len(s):
        return s[i] == s[j]
    return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))