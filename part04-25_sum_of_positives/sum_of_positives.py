# Write your solution here
def sum_of_positives(list1):
    return sum(num for num in list1 if num > 0)

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
        