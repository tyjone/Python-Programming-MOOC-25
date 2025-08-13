# Write your solution here
def mean(lists : list):
    list_of_mine = lists
    return sum(list_of_mine)/len(list_of_mine)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)