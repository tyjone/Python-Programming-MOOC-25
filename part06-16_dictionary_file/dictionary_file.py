# Write your solution here
# Load existing entries from the file
dictionary = []

try:
    with open("dictionary.txt", "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 2:
                dictionary.append((parts[0], parts[1]))
except FileNotFoundError:
    pass  # If the file doesn't exist yet, start with an empty dictionary

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    choice = input("Function: ")

    if choice == "1":
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        dictionary.append((finnish, english))
        with open("dictionary.txt", "a") as file:
            file.write(f"{finnish}:{english}\n")
        print("Dictionary entry added")

    elif choice == "2":
        term = input("Search term: ")
        found = False
        for finnish, english in dictionary:
            if term in finnish or term in english:
                print(f"{finnish} - {english}")

                found = True
        if not found:
            print("No entries found")

    elif choice == "3":
        print("Bye!")
        break

    else:
        print("Invalid option")
