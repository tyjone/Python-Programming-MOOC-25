# Write your solution here
def everything_reversed(list1):
    return ["".join(reversed(string)) for string in reversed(list1)]



if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)

