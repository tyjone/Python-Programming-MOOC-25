# Write your solution here
def find_words(search_term: str) -> list:
    result = []

    # Load all words from the file
    with open("words.txt", "r") as file:
        words = [line.strip() for line in file]

    # Handle dot wildcard
    if "." in search_term:
        import re
        pattern = f"^{search_term}$"
        regex = re.compile(pattern)
        result = [word for word in words if regex.match(word)]

    # Handle asterisk wildcard
    elif search_term.startswith("*"):
        suffix = search_term[1:]
        result = [word for word in words if word.endswith(suffix)]

    elif search_term.endswith("*"):
        prefix = search_term[:-1]
        result = [word for word in words if word.startswith(prefix)]

    # Handle exact match
    else:
        result = [word for word in words if word == search_term]

    return result
