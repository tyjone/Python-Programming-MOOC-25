# Write your solution here
book = {}

while True:
    command = input("command (1 search, 2 add, 3 quit): ")

    if command == "2":
        name = input("name: ")
        number = input("number: ")
        if name in book:
            book[name].append(number)  # Add to existing list
        else:
            book[name] = [number]  # Create new list
        print("ok!")

    elif command == "1":
        name = input("name: ")
        if name in book:
            for num in book[name]:
                print(num)
        else:
            print("no number")

    elif command == "3":
        print("quitting...")
        break

    else:
        print("invalid command")


