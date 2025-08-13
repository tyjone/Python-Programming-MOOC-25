# Write your solution here
def palindromes(word):
    # Returns True if the word is the same forwards and backwards
    return word == word[::-1]

# Main program
while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")


# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
