# Write your solution here
def length_of_longest(strings):
    return max(len(s) for s in strings)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)