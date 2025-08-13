# Write your solution here
def invert(dictionary: dict):
    invert_dictionary = {}
    for key,value in dictionary.items():
        invert_dictionary[value] = key
    dictionary.clear()
    dictionary.update(invert_dictionary)


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)