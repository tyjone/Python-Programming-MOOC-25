# Write your solution here
def all_the_longest(strings):
    max_length = max(len(s) for s in strings)
    return [s for s in strings if len(s) == max_length]


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']