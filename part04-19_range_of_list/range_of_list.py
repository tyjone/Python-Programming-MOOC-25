# Write your solution here
def range_of_list(lists : list):
    list_of_mine = lists
    return max(list_of_mine) - min(list_of_mine)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)