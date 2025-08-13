# Write your solution here
my_list = []
num = 1
while True:
    print(f"The list is now {my_list}")
    options = input("a(d)d, (r)emove or e(x)it: ")
    if options == "d":
        my_list.append(num)
        num += 1
    elif options == "r":
        my_list.pop(-1)
        num -= 1
    elif options == "x":
        print("Bye!")
        break