# Write your solution here
def shortest(strings):
    return min(strings, key=len)


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)