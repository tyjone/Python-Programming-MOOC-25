# Write your solution here
my_list = [1, 2, 3, 4, 5]
while True:
    my_index = int(input("Index: "))
    if my_index == -1:
        break
    new_value = int(input("New value: "))
    my_list[my_index] = new_value
    print(my_list)


