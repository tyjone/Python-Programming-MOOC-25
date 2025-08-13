# Create a list of words
wordlist = set()

# Add lower cased words into the list
with open("wordlist.txt") as file:
    for line in file:
        wordlist.add(line.strip().lower())


text = input("Write text: ")

words = text.split()
checked = []

for word in words:
    # Remove punctuation for spell-checking (optional enhancement)
    stripped = ''.join(char for char in word if char.isalpha())

    if stripped.lower() in wordlist:
        checked.append(word)
    else:
        checked.append(f"*{word}*")

print(" ".join(checked))
