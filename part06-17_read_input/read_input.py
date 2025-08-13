# Write your solution here
def read_input(prompt, lower, upper):
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            if lower <= number <= upper:
                return number
            else:
                print(f"You must type in an integer between {lower} and {upper}")
        except ValueError:
            print(f"You must type in an integer between {lower} and {upper}")
