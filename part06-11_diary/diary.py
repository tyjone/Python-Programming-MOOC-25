# Write your solution here
while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    choice = input('Function: ')
    if choice == '1':
        entry = input('Diary entry: ')
        with open('diary.txt', 'a') as file:
            file.write(entry + '\n')
    elif choice == '2':
        with open('diary.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    elif choice == '0':
        print("Bye now!")
        break

        
