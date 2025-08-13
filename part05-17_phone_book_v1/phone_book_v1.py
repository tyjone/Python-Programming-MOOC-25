# Write your solution here
book = {}
while True:
    command = input("command (1 search, 2 add, 3 quit): ")
    
    if command == "2":
        name = input("name: ")
        number = input("number: ")
        book[name] = number
        print("ok!")
        print(book)

    elif command == "1":
        name_search = input("name: ")
        if name_search in book:
            print(book[name_search])
        else:
            print("no number")

    elif command == "3":
        print("quitting...")
        break

    else:
        print("invalid command")

