# Write your solution here
def list_sum(list1, list2):
    return [x + y for x, y in zip(list1, list2)]


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]